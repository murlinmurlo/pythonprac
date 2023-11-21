def objcount(cls):
    class NewClass(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            NewClass.counter += 1

        def __del__(self):
            NewClass.counter -= 1
            #super().__del__()

    return NewClass

import sys
exec(sys.stdin.read())
