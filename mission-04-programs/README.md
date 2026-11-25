# Mission 4 — How programs run

## 1. Task / objective

Run a one-line Python program and explain what compilers and interpreters do.

## 2. Work completed

Created and ran [hello.py](hello.py). It printed the expected message.

## 3. Commands / tools used

From the mission folder, `python3 hello.py` ran the saved source file. The `print()` function wrote one line to the terminal.

```text
$ python3 hello.py
Hello from Python
```

## 4. My understanding

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation or execution happens | Translates code before that compiled result executes. | Carries out instructions during execution. |
| Typical output | Machine code, object code or bytecode, depending on the compiler. | The program's runtime output or effects, such as terminal text. |
| Example | Clang compiling C to an executable. | CPython executing Python bytecode. |
| Advantage | The compiled result can be reused, and the compiler can optimize it. | It makes it straightforward to run a script or try an expression interactively. |

A compiler changes code into a form another component can run. An interpreter carries out instructions and produces the program's effects while the program runs. CPython uses both ideas: it first compiles source to bytecode, and its interpreter executes that bytecode.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[hello.py](hello.py) and its verified output above.

## 8. Commit details

Pushed to GitHub on `main`. [`Compare compilers and interpreters`](https://github.com/Illtrapx/digital-detective-8489/commit/f8873011ff5e361d9afe7ff6ed0d89781742f277).
