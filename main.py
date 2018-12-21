from parser import parser
from scanner import scanner

def main():
    s = scanner('sample_input.txt')
    tokens, types = s.arrOut()
    p = parser(tokens, types)
    p.drow()

if __name__ == "__main__":
    main()