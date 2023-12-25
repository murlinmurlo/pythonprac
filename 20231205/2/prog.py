import asyncio as a
import copy as c
import random as r

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i, j, k = start, middle, start
    while i < middle or j < finish:
        if j == finish or (i < middle and A[i] < A[j]):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    event_out.set()


async def mtasks(prev_A):
    A = c.deepcopy(prev_A)
    B = [0] * len(A)
    tasks, events = [], []

    for i in range(len(A) + 1):
        events.append(a.Event())
        events[i].set()

    cur_len, flag = 1, True
    while cur_len < len(A):
        i = 0
        new_events = []
        for start in range(0, len(A), 2 * cur_len):
            middle = min(start + cur_len, len(A) - 1)
            finish = min(start + cur_len * 2, len(A))
            new_events.append(a.Event())

            if flag:
                tasks.append(a.create_task(merge(A, B, start, middle, finish, events[i], events[i + 1], new_events[-1])))
            else:
                tasks.append(a.create_task(merge(B, A, start, middle, finish, events[i], events[i + 1], new_events[-1])))
            i += 2
            if finish == len(A):
                break

        new_events.append(new_events[-1])
        events = new_events
        flag = not flag
        cur_len *= 2

    if flag:
        return tasks, A
    else:
        return tasks, B

import sys
exec(sys.stdin.read())
