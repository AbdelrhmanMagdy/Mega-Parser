from parser import parser
from scanner import scanner

def main():
    file_name = sys.argv[1] if len(sys.argv)>1 else 'sample_input.txt'
    s = scanner(file_name)
    tokens, types = s.arrOut()
    p = parser(tokens, types)
    p.drow()

if __name__ == "__main__":
    main()