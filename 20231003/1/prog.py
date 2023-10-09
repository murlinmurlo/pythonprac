
def Pareto(*pairs):
    pareto_front = []
    for i in range(len(pairs)):
        is_dominated = False
        for j in range(len(pairs)):
            if pairs[j][0] >= pairs[i][0] and pairs[j][1] >= pairs[i][1] and (pairs[j][0] > pairs[i][0] or pairs[j][1] > pairs[i][1]):
                is_dominated = True
                break
        if not is_dominated:
            pareto_front.append(pairs[i])
    return tuple(pareto_front)

print(Pareto(*eval(input())))
