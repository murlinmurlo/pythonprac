Python 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0)

>>> next(ite)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
  File "/home/masha/Python3-tasks/0/1.py", line 4, in walk2d
    dx, dy = yield (x, y)
TypeError: cannot unpack non-iterable NoneType object
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "/home/masha/Python3-tasks/0/1.py", line 10, in <module>
    r1 = generator.send((1, 0)) 
NameError: name 'generator' is not defined
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0)
(1, 0) (1, 1)
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0)
(1, 0) (1, 1)
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0) (1, 0) (1, 1)
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "/home/masha/Python3-tasks/0/1.py", line 11, in <module>
    r0 = ite.send((2, 3))
TypeError: can't send non-None value to a just-started generator
>>> 
=================== RESTART: /home/masha/Python3-tasks/0/1.py ==================
(0, 0) (1, 0) (1, 1)
