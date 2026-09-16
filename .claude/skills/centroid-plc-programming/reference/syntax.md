# Centroid PLC Language: Syntax Reference

Source: `docs/official/centroid_plc_programming_manual.pdf` (PLC Manual, rev8 07/24/26). The
manual prints no page numbers; citations below are PDF page numbers, verified with
`pdftotext -layout -f N -l N docs/official/centroid_plc_programming_manual.pdf -`.

---

## Execution Model

The PLC program is a flat, sequential list of `IS` definitions followed by `IF`/`THEN`
statements. It runs from top to bottom and executes every line except logic inside a Stage,
which the executor skips whenever that Stage is RST (PLC Manual, PDF p.30, p.16).

- Code inside a regular Stage (`STG`) executes 50 times per second. Code inside a Fast Stage
  (`FSTG`) or outside any Stage executes up to 1000 times per second (PLC Manual, PDF p.13).
- Fast Stages do not interrupt normal-speed Stages: if the rest of the program takes longer than
  1 ms to run, Fast Stages will not actually hit the 1000/s rate (PLC Manual, PDF p.16).
- Timers, and the real-world physical state of Inputs and Outputs, are buffered at the start of
  the pass and hold that value for the whole pass. Memory Bits, all Words, One-Shots, both kinds
  of Stages, System Variables, and the in-program image of the Outputs update immediately — a
  later line in the same pass sees the value an earlier line wrote (PLC Manual, PDF p.13).
- `STG1` is SET automatically at startup (PLC Manual, PDF p.13).

When a Stage is RST, any variables it last SET or RST hold that state until changed elsewhere in
the program. No checks are made against resetting every Stage at once, so the program can end up
with nothing running (PLC Manual, PDF p.16).

```
IF 1==1 THEN SET STG1   ; PLC Manual, PDF p.16
```

---

## Statement Forms

### 1. Definition — `Name IS Resource`

Used only in the definition section at the top of the program, before the first `IF` statement.
Any definition after the first `IF`/`THEN` is a compile-time error (PLC Manual, PDF p.17).

```
EStopOk_I  IS INP11    ; PLC Manual, PDF p.17
Lube_O     IS OUT2      ; PLC Manual, PDF p.17
```

Constant definitions may use math, and may reference an already-defined constant, as long as the
whole expression is in parentheses:

```
DEFINED_CONSTANT_C IS (1+2+5*7)              ; PLC Manual, PDF p.17
SECOND_CONST_C     IS (DEFINED_CONSTANT_C*10) ; PLC Manual, PDF p.17
```

### 2. Conditional statement — `IF <condition> THEN <action>[, <action>]*`

The first `IF`/`THEN` in a program marks the end of the definition section. The part between
`IF` and `THEN` must resolve to a boolean; a bare Word cannot be tested this way — it must be
compared with a Relational Operator (PLC Manual, PDF p.17):

```
IF W1 > 10 THEN (OUT2)   ; valid   — PLC Manual, PDF p.17
IF W1 THEN (OUT2)        ; invalid — PLC Manual, PDF p.17
```

There is no `ELSE` keyword. The manual's stated workaround is to copy the condition onto a
second line and negate it with `!` (PLC Manual, PDF p.17).

### 3. Word assignment — `<Word or Timer> = <expression>`

Assigns a Word, Timer or numeric value to a Word or Timer, as an action after `THEN`
(PLC Manual, PDF p.21).

```
IF 1==1 THEN W1 = 10    ; PLC Manual, PDF p.21
IF 1==1 THEN T1 = W1    ; PLC Manual, PDF p.21
IF 1==1 THEN FW1 = 2.5  ; PLC Manual, PDF p.21
```

### 4. Output coil — `(<bit-var>)`

Parentheses on the action side of `THEN` form a coil: the variable is SET if the condition is
true and RST if it is false. Coils cannot be used on Words or on Timers, since a Timer coiled
this way is generally guaranteed to be turned off again on the next pass (PLC Manual, PDF p.22).

```
IF 1==1 THEN (OUT1)   ; always SET OUT1        — PLC Manual, PDF p.22
IF MEM1 THEN (OUT2)   ; SET/RST with MEM1      — PLC Manual, PDF p.22
```

Do not coil a variable on one line and also `SET`/`RST` it elsewhere: the value "will change while
moving through the PLC program and may have surprising results." All the logic to turn a coiled
variable on or off must be on the same line (PLC Manual, PDF p.22).

### 5. Jump — `JMP <stage>`

RSTs the current Stage and SETs the named Stage. Execution does not jump within the pass; it
continues on the next line, and "typically the stages are written one after the other so in
essence it will move to that one" (PLC Manual, PDF p.22). The manual advises against `JMP`-ing
out of `MainStage`, but expects it from `InitialStage` (PLC Manual, PDF p.22).

```
IF 1==1 THEN JMP MainStage   ; PLC Manual, PDF p.23
```

---

## Operators

### Logical Operators

Apply to bit-type variables, including System Variables that are bits; cannot be used on Word
types (PLC Manual, PDF p.23-24).

| Symbol | Meaning | Example |
|--------|---------|---------|
| `&&` | AND — both sides true | `IF MEM1 && INP2 THEN (OUT1)` (PLC Manual, PDF p.24) |
| `\|\|` | OR — either side true | `IF (W1 > W2) \|\| !MEM4 THEN (OUT5)` (PLC Manual, PDF p.24) |
| `!` | NOT (unary) | inverts a bit (PLC Manual, PDF p.24) |
| `XOR` / `^` | Exclusive OR — exactly one side true | truth table (PLC Manual, PDF p.24) |

A Relational comparison result can be combined with Logical Operators, and parentheses may be
used to group terms (PLC Manual, PDF p.24).

### Relational Operators

Apply to Words, Word-type System Variables and Timers only; bit-type variables cannot be
compared this way (PLC Manual, PDF p.23).

| Symbol | Meaning |
|--------|---------|
| `==` | Exactly equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

`==` and `!=` on Floating-point Words are likely to fail from rounding error; the manual
recommends `>=`/`<=` instead (PLC Manual, PDF p.23). Comparing a Timer with a Relational
Operator checks its current elapsed count in milliseconds, not whether it has expired
(PLC Manual, PDF p.23).

### Arithmetic Operators

`*`, `/`, `+`, `-`, `%` are binary operators that apply to Word types only (PLC Manual, PDF p.23).
Assigning a floating-point result to an integer Word truncates the decimal portion:
`IF 1==1 THEN W1 = 2.5*1` sets `W1` to `2` (PLC Manual, PDF p.23). Arithmetic can also appear
inside a Relational expression in a condition, e.g.
`IF !((ErrorCode_W % 256 == 1) || (ErrorCode_W % 256 == 2)) THEN JMP BadErrorStage`
(PLC Manual, PDF p.98).

### Assignment Operator

`=` sets a Word or Timer on the left to a Word, Timer, or numeric value on the right
(PLC Manual, PDF p.21).

---

## Conditions vs. Actions

### What may appear in the condition (between `IF` and `THEN`)

Any bit-type variable directly (Input, Output, Memory Bit, Stage, Fast Stage, SV bit, One-Shot), a
Timer directly or with a Relational Operator, or a Relational expression on a Word, Double Word,
Floating-point Word, Double-Floating-point Word or SV Word, combined with Logical Operators
(PLC Manual, PDF p.17-18):

```
IF INP50 THEN (OUT50)          ; PLC Manual, PDF p.17
IF W1 > 156 THEN (OUT30)       ; PLC Manual, PDF p.17
IF FW1 > 5.432 THEN SET OUT3   ; PLC Manual, PDF p.17
```

### What may appear as an action (after `THEN`, comma-separated)

| Action form | Effect |
|-------------|--------|
| `SET <bit-var>` | Unconditionally turns the variable on (PLC Manual, PDF p.21) |
| `RST <bit-var>` | Unconditionally turns the variable off (PLC Manual, PDF p.22) |
| `<word-var> = <expression>` | Assigns a computed value to a Word or Timer (PLC Manual, PDF p.21) |
| `(<bit-var>)` | Coil: SET if the condition is true, RST if false (PLC Manual, PDF p.22) |
| `JMP <stage>` | RSTs the current Stage, SETs the named Stage (PLC Manual, PDF p.22) |
| `MSG <word-var>` | Sends the Word's message value to the CNC operator display (PLC Manual, PDF p.18) |

`SET` and `RST` apply to Outputs, Memory Bits, Inputs, Timers, Stages, Fast Stages and System
Variables that are bits; One-Shots cannot be `SET` or `RST` directly and may only be turned on or
off with a coil (PLC Manual, PDF p.15, p.21-22).

> p.21-22's prose says One-Shots cannot be `SET` or `RST`, but the "Data Types that can be used
> with SET/RST" tables on those same pages list `One-Shots | IF 1==1 THEN SET PD2` and
> `One-Shots | IF 1==1 THEN RST PD2` (PLC Manual, PDF p.21-22). The manual contradicts itself.

---

## Comments

A comment begins with `;` and runs to the end of the line; a comment that continues onto the next
physical line starts that line with `;` again, as in this manual example (PLC Manual, PDF p.15):

```
IF MEM1 THEN SET T1                  ;Set the value that the timer counts to before evaluating to
                                     ;true.
```

Section explanations shorter than about five lines are prefixed `;` with
no space; longer ones are bracketed above and below by a full-width line of `-` characters, with
every line inside starting with `;` (PLC Manual, PDF p.31).

### Programming conventions

The manual's own naming, Stage-header and layout conventions (PLC Manual, PDF p.30):

- **Naming:** Constants `SCREAMING_SNAKE_CASE` ending `_C`; Inputs/Outputs/Memory
  Bits/Words/Timers/Stages in `PascalCase` with a type suffix (`_I`, `_O`, `_M`, `_W`, `_DW`,
  `_FW`, `_DFW`, `_T`, `_PD`, `Stage`/`_STG`, `Stage`/`_FSTG`); defined System Variables suffixed
  `_SV` (PLC Manual, PDF p.30-31).
- **Stage header:** the Stage name is typed 20 columns from the left, with a full-width line of
  `=` characters above and below it (PLC Manual, PDF p.31).
- **Section title:** a full-width line of `-` characters, with the title starting after 5 dashes
  (PLC Manual, PDF p.31).
- **Definition alignment:** the `IS` keyword lines up with the other `IS` keywords in its
  section (not the whole file), with two spaces between the longest name in that section and
  `IS`; trailing comments are lined up as well (PLC Manual, PDF p.31).
- **General formatting:** lines stay at or under 79 columns; spaces only, never tabs; variable
  name capitalization is not compiler-enforced but should be kept consistent
  (PLC Manual, PDF p.31).
