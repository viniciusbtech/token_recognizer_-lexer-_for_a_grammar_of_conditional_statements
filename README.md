# Lexer for Conditional Statements

<img width="799" height="489" alt="image" src="https://github.com/user-attachments/assets/08eba1ad-e580-4158-ba44-e340e141d3a9" />


This project implements a token recognizer (lexer) for a grammar of conditional statements using the **PLY (Python Lex-Yacc)** library.

## Requirements

- Python 3.x
- PLY (`pip install ply`)

## Supported Grammar

The recognized grammar is based on Slide 22 of the course:

- `stmt -> if expr then stmt | if expr then stmt else stmt | epsilon`
- `expr -> term relop term | term`
- `term -> id | number`

## Tokens and Attributes

Tokens are displayed in the format `<token_name, attribute_value>`, according to Slide 23:

- `if`, `then`, `else`: `<token, ->`
- `id`, `number`: `<token, pointer to table entry X>`
- `relop`: `<relop, ATTRIBUTE>`, where ATTRIBUTE can be `LT`, `LE`, `EQ`, `NE`, `GT`, `GE`.

## How to Run

1. Make sure the `ply` library is installed:
   ```bash
   pip install ply
   ```

2. Run the script `lexer.py`:
   ```bash
   python lexer.py
   ```

3. To process a specific text file:
   ```bash
   python lexer.py filename.txt
   ```

## Example Output

For the input `if x <= 10.0 then x = 100`:

```
<if, ->
<id, pointer to table entry 1>
<relop, LE>
<number, pointer to table entry 2>
<then, ->
<id, pointer to table entry 1>
<relop, EQ>
<number, pointer to table entry 3>
```
