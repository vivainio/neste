# neste
Command line application to pretty print brace nested files (of any syntax)

Sometimes you have an expression in whatever syntax that supports balances braces () {} [], but is otherwise uninteresting (say, you may have a custom parser for proprietary expression language). You can use this tool to check and pretty print such files and expressions.

As a special case, semicolons also force a linebreak (as they often are meant to be).

Example expression 

```
SUM((B2:B10>=A2:A10) * (B2:B10>0))
```

Is rendered as:

```
SUM
(
  (
    B2:B10>=A2:A10
  )
  *
  (
    B2:B10>0
  )
)
```

This is intended to make checking and visually parsing complex expressions easier.

# Installation

```
pip install neste-braces
```

# Usage

Invoke with file name, or use as stdin filter without any arguments.

```
PS C:\r\neste> echo "hello ( world {} )" | neste
hello
(
  world
  {}
)

```

Or

```
$ neste foo.txt 

```

# License

MIT