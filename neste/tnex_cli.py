import sys
import glob
import yaml
import re
from .tnex import parse, expand_xml_entities

def main():
    files = glob.glob(sys.argv[1], recursive=True)
    for f in files:
        print(f)
        try:
            cont = open(f).read()
        except UnicodeDecodeError:
            print("READ FAILED")
        expressions = re.findall("{(.*?)}", cont)
        for e in expressions:
            print(">", e)
            try:
                parsed = parse(expand_xml_entities(e))
                rendered = yaml.dump(parsed)
                print(rendered)
            except ValueError as exc:
                print(exc)
    print(files)
    ...

if __name__ == "__main__":
    main()
