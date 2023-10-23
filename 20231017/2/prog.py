from math import *

class FunctionDictionary:
    def __init__(self):
        self.dictionary = {}
        self.functions = 1
        self.strings = 1

    def define_function(self, func_name, args, expr):
        self.functions += func_name not in self.dictionary
        self.dictionary[func_name] = (args, expr, len(args) == 1)

    def execute_expression(self, func_name, args):
        self.strings += 1

        args_letters, expr, is_single_arg = self.dictionary[func_name]

        for i in range(len(args)):
            exec(f"{args_letters[i]} = {args[i]}")
        
        result = eval(expr)
        print(result)

    def run(self):
        while True:
            s = input()
            if s.split()[0] == 'quit':
                break

            if s[0] == ':':
                func_name, *args, expr = s.split()
                func_name = func_name[1:]
                self.define_function(func_name, args, expr)
            else:
                if ' ' not in s:
                    func_name = s
                else:
                    func_name = s[:s.index(' ')]
                    if self.dictionary[func_name][2]:
                        args = [s[s.index(' ') + 1:]]
                    else:
                        func_name, *args = s.split()
                self.execute_expression(func_name, args)

        print("{} {}".format(self.functions, self.strings))

function_dict = FunctionDictionary()
function_dict.run()
