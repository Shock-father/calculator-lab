# main.py
from calculator import core


def repl():
    print("Simple calculator. Commands: add, sub, mul, div  Example: add 2 3")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not line:
            continue
        if line in ("q", "quit", "exit"):
            print("Exiting.")
            break
        parts = line.split()
        if len(parts) != 3:
            print("Usage: <op> <num1> <num2>  e.g., add 2 3")
            continue
        op, a_s, b_s = parts
        try:
            a = float(a_s)
            b = float(b_s)
            func = {"add": core.add, "sub": core.sub,
                    "mul": core.mul, "div": core.div}.get(op)
            if func is None:
                print("Unknown op. Use: add, sub, mul, div")
                continue
            print(func(a, b))
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    repl()
