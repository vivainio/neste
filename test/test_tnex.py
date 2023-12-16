from neste.tnex import parse

def test_tokenize():
    assert parse("foo") == ["foo"]
    assert parse("foo(1;1)") == [["foo", "1", "1"]]
    assert parse('"some string"') == ['"some string"']
    assert parse('"foo";0') == ['"foo"', "0"]
    assert parse("foo(1);2") == [["foo", "1"], "2"]
    assert parse('foo("some string";"other string";0)') == [
        ["foo", '"some string"', '"other string"', "0"]
    ]
    assert parse('foo("some string";"other string");1') == [
        ["foo", '"some string"', '"other string"'],
        "1",
    ]
    # nothing special with ,
    assert parse("a,b(c,d;e,f;1.0)") == [['a,b', 'c,d', 'e,f', '1.0']]

    assert parse(r'" string with \" char"') == ['" string with \\" char"']
    assert parse(r'"some string with ) and ( and \" characters"') == [
        '"some string with ) and ( and \\" characters"'
    ]

    assert parse(r'foo,"long / () accessor"') == ['foo,"long / () accessor"']

    complex = parse(
        r'foo(f1;bar(b1;b2;"b3";"wide string");f2;baz(1;"some string with ) and ( and \" characters")));top1'
    )
    assert complex == [
        [
            "foo",
            "f1",
            ["bar", "b1", "b2", '"b3"', '"wide string"'],
            "f2",
            ["baz", "1", '"some string with ) and ( and \\" characters"'],
        ]
    ]
