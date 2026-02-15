# oo2c Compiler

## Description
The **oo2c Compiler** is an educational compiler that translates a simplified
object-oriented language (**oo2c**) into the procedural language **C**.

The project was developed for the course **“Compilers II”**
at the **University of Ioannina** using **ANTLR** and **Python**.

---

## Features
- Object-oriented to C translation
- Lexical, Syntax and Semantic Analysis
- Code Generation to C
- Support for classes, inheritance, constructors and methods
- Control structures: if, while, return, print
- Expression and condition evaluation

---

## Technologies
- Python
- ANTLR
- C
- Formal Grammars

---

## How to Run

### Requirements
- Python 3.8+
- Java (for ANTLR)

### Steps
1. Generate parser with ANTLR:
```
java -jar antlr-4.13.2-complete.jar oos.g4
```

2. Run the compiler:
```
python oosExecute.py complex.oos
```

3. Output C file will be generated in the project directory.

---

## Project Structure
```
oo2c_compiler
├── oosLexer.py
├── oosParser.py
├── oosExecute.py
├── complex.oos
├── complex.c
└── antlr-4.13.2-complete.jar
```

---

## Educational Purpose
This project demonstrates compiler construction concepts such as:
- Parsing
- Semantic Analysis
- Code Generation
- Grammar Design
