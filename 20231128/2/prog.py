import math

def interpret(program):
    commands = []
    labels = {}
    variables = {}

    # Первый проход: составление списка команд и проверка меток
    for line in program:
        line = line.strip()
        if line.endswith(":"):
            label = line[:-1]
            labels[label] = len(commands)
        else:
            commands.append(line)

    # Второй проход: интерпретация команд
    pc = 0
    while pc < len(commands):
        command = commands[pc].split()
        opcode = command[0]

        if opcode == "stop":
            break
        elif opcode == "store":
            value = float(command[1])
            receiver = command[2]
            variables[receiver] = value
        elif opcode in ["add", "sub", "div", "mul"]:
            source = variables.get(command[1], 0)
            operand = variables.get(command[2], 0)
            receiver = command[3]

            if opcode == "add":
                result = source + operand
            elif opcode == "sub":
                result = source - operand
            elif opcode == "div":
                if operand != 0:
                    result = source / operand
                else:
                    result = math.inf
            elif opcode == "mul":
                result = source * operand

            variables[receiver] = result
        elif opcode.startswith("if"):
            source = variables.get(command[1], 0)
            operand = variables.get(command[2], 0)
            label = command[3]

            if opcode == "ifeq" and source == operand:
                pc = labels[label]
            elif opcode == "ifne" and source != operand:
                pc = labels[label]
            elif opcode == "ifgt" and source > operand:
                pc = labels[label]
            elif opcode == "ifge" and source >= operand:
                pc = labels[label]
            elif opcode == "iflt" and source < operand:
                pc = labels[label]
            elif opcode == "ifle" and source <= operand:
                pc = labels[label]
        elif opcode == "out":
            source = variables.get(command[1], 0)
            print(source)

        pc += 1

# Пример использования
program = [
    "store 100 i",
    "store 1 I",
    "store 1 f",
    "",
    "loop:",
    "div I f a",
    "add e a e",
    "add n I n",
    "mul f n f",
    "",
    "sub i I i",
    "ifge i I loop",
    "out e"
]

interpret(program)
