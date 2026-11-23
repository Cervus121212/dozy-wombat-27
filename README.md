# The One-Line Laugh

Entry for the make.fun bounty
[u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/competitions/u-ronigrv-the-one-line-laugh-7ccca46f)
("The One-Line Laugh", $5 over the top three).

## The entry

One funny line, at most 200 characters, on any subject. This one:

> My password manager forgot my master password, so now we are both locked out of my life together.

97 characters, one sentence. The tool built to remember passwords forgets
the one password that matters, and the twist lands in the last word: the
manager and I are locked out *together*. It names an everyday truth
(password fatigue) with a surprise at the end that still makes sense, and
no word is there to explain the joke.

## How it works

`main.py` is deterministic and standard library only. It builds the line
from two parts (setup, then punchline) and writes it to
`/output/entry.txt`, then sets the file to mode 0644 so the grader can
read it. It never touches the permissions of `/output` itself and never
removes anything.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT
