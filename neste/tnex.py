import re

def tokenize(s: str):
    # negative lookbehind for \ escaping, split to parts separated by ; ( ) "
    tokens = re.split(r"((?<!\\)[\(\)\";])", s)
    return list(filter(None, tokens))


def _parse_string(toks: list[str]):
    assert toks[0] == '"'
    # eat up tokens to produce just one str
    end_token_index = toks.index('"', 1)
    stringparts = toks[0 : end_token_index + 1]
    value = "".join(stringparts)
    return value, len(stringparts)

def _parse_accessor(toks: list[str]):
    if toks[1] == '"':
        s, moved = _parse_string(toks[1:])
        return toks[0] + s, moved + 1
    
    return toks[0],1

def emit_nested_sequence(parts: list[str]):
    res = []
    i = 0
    while i < len(parts):
        it = parts[i]
        if it == '"':
            s, moved = _parse_string(parts[i:])
            res.append(s)
            i += moved
        elif it == ";":
            i += 1
        elif it == ")":
            i += 1
            break
        elif it == "(":
            nested, moved = emit_nested_sequence(parts[i + 1 :])
            nested.insert(0, parts[i - 1])
            res = res[0:-1]
            res.append(nested)
            i += moved
        # special foo,"hello" accessor that accesses property of foo
        elif it.endswith(","):
            s,moved = _parse_accessor(parts[i:])
            res.append(s)
            i+=moved
        else:
            res.append(it)
            i += 1

    return (res, i + 1)



def parse(s: str):
    tokens = tokenize(s)
    parsed, _ = emit_nested_sequence(tokens)
    return parsed

def expand_xml_entities(xml_string: str):
    entity_pattern = re.compile(r'&([^;]+);')

    def replace_entity(match: re.Match):
        entity = match.group(1)
        if entity == 'lt':
            return '<'
        elif entity == 'gt':
            return '>'
        elif entity == 'amp':
            return '&'
        elif entity == "quot":
            return '"'
        else:
            return match.group(0)

    expanded_xml = entity_pattern.sub(replace_entity, xml_string)
    return expanded_xml

