commands = set('><+-.,[]')


def preprocess(code):
    return ''.join([c for c in code if c in commands])

def buildBracketMap(code):
    stack = []
    bracketMap = {}
    
    for pos, cmd in enumerate(code):
        if cmd == '[':
            stack.append(pos)
        elif cmd == ']':
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {pos}")
            start = stack.pop()
            bracketMap[start] = pos
            bracketMap[pos] = start
    
    if stack:
        raise SyntaxError(f"Unmatched '[' at position {stack[-1]}")

    return bracketMap
    

def brainfuck():
    userInput = input('Enter code: ')
    tape = [0] * 300000
    pointer = 0
    pc = 0
    code = preprocess(userInput)
    try:
        bracketMap = buildBracketMap(code)
    except SyntaxError as e:
        print('The input code is not valid.')
        return
    
    while pc < len(code):
        cmd = code[pc]
        if cmd == '>':
            pointer += 1
        elif cmd == '<':
            pointer -= 1
        elif cmd == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif cmd == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif cmd == '.':
            print(chr(tape[pointer]), end='')
        elif cmd == ',':
            inp = input("Input: ")
            tape[pointer] = ord(inp[0]) if inp else 0
        elif cmd == '[' and tape[pointer] == 0:
            pc = bracketMap[pc]
        elif cmd == ']' and tape[pointer] != 0:
            pc = bracketMap[pc]
        pc += 1

brainfuck()
