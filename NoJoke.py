# no_joke.py - Interpreter cho "No Joke"

import sys
import random

variables = {}

def interpret(line):
    tokens = line.strip().split()

    if not tokens:
        return

    if tokens[0] == "SET":
        # SET X TO 5
        if len(tokens) >= 4 and tokens[2] == "TO":
            var_name = tokens[1]
            try:
                value = int(tokens[3])
            except ValueError:
                value = variables.get(tokens[3], 0)
            variables[var_name] = value

    elif tokens[0] == "TRUST" and tokens[1] == "ME":
        # TRUST ME ADD X AND Y
        if len(tokens) >= 6 and tokens[2] == "ADD":
            a = tokens[3]
            b = tokens[5]
            if random.choice([True, False]):
                result = variables.get(a, 0) + variables.get(b, 0)
                variables["RESULT"] = result
                print("Okay... I guess I added them.")
            else:
                print("Nah, not today.")

    elif tokens[0] == "NO" and tokens[1] == "JOKE":
        if tokens[2] == "PRINT":
            var = tokens[3]
            value = variables.get(var, None)
            if value is None:
                print(" I don't even know what", var, "is.")
            else:
                print("Totally serious output:", value)

    elif tokens[0] == "LAUGH" and tokens[1] == "IF":
        # LAUGH IF X EQUALS Y
        if len(tokens) >= 5 and tokens[3] == "EQUALS":
            a = variables.get(tokens[2], 0)
            b = variables.get(tokens[4], 0)
            if a != b:
                print(" Because", a, "≠", b)
            else:
                print(" Too equal to laugh.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python no_joke.py <filename.nojoke>")
        return

    filename = sys.argv[1]
    try:
        with open(filename) as f:
            for line in f:
                interpret(line)
    except FileNotFoundError:
        print("File not found:", filename)

if __name__ == "__main__":
    main()

