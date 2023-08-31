import re,sys


def render(cont: str):
    tokens = re.split("([\{\(\}\)\[\];])",cont)
    tokens = [t.strip() for t in tokens if t.strip()]
    indent = 0

    stack = []
    enders = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }

    braces = set()

    braces.update(enders.keys())
    braces.update(enders.values())

    # simplify round, merge () and single ;

    for i,t in enumerate(tokens):
        if not t:
            continue
        if t in enders and tokens[i+1] == enders[t]:
            tokens[i] = t + tokens[i+1]
            tokens[i+1] = None
        if t == ";" and tokens[i-1] and ";" not in tokens[i-1]:
            tokens[i] = None
            tokens[i-1] = tokens[i-1]+" ;"

    # remove nones
    tokens = [t for t in tokens if t]


    for t in tokens:
        t = t.strip()
        if not t:
            continue

        brace = t.strip(" ;")
        if brace == "}" or brace == ")":
            indent -= 1
            got = stack.pop()
            expected = enders[got]
            if brace != expected:
                print("ERROR: Expected", expected, "got", t)


        print(indent * "  " + t)

        if brace == "{" or brace == "(":
            indent += 1
            stack.append(brace)

        
def main():        
    cont = open(sys.argv[1]).read()
    render(cont)

if __name__ == "__main__":
    main()