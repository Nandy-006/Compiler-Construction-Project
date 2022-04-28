<h1 align="center" style="text-decoration:none;"> 
    <b>CS F363 Compiler Construction</b>
    <br>
    Programming Assignment
</h1></center>
<br>

## Team Members

<li>[2019A7PS0086H] Amogh Bharadwaj </li>
<li>[2019A7PS0164H] Nandan H R </li>
<li>[2019A7PS0033H] T V Chandra Vamsi</li>

<br>

## Running the compiler:

```
usage: python3 compile.py [-h] [--tokenize] [--parseOnly] [--tokenPath TOKENPATH] [--stackPath STACKPATH] [--ICPath ICPATH] filepath

Langwej frontend compiler.

positional arguments:
  filepath              Specifies the path to the .lwj file to be compiled

optional arguments:
  -h, --help            show this help message and exit
  --tokenize            Specify this flag if the program needs to be tokenized only, defaults to False
  --parseOnly           Specify this flag if intermediate code should not be generated, defaults to False
  --tokenPath TOKENPATH
                        Specifies the file where tokens are written, defaults to parseTokens.txt
  --stackPath STACKPATH
                        Specifies the file where parse stack traces are written, defaults to parseStack.txt
  --ICPath ICPATH       Specifies the path where intermediate code generated is written, defaults to parseIC.txt
```

## Error Recovery for Parser:

### 1. Error recovery for extra closing parenthesis (error code e0):

<b>Examples</b>:
```
let x = (a + b));
               ^
whil (a > b) { a = a + 1); }
                        ^
```

<b>Recovery Method:</b>
<ol>
<li>Report the error.</li>
<li>Skip the closing parenthesis and get the next token.</li>
<li>Continue parsing.</li>
</ol>

### 2. Error recovery for extra closing brace (error code e1):

<b>Examples</b>:
```
if (a > b) { a = a + 1; }} else { a = a - 1; }
                         ^
intijur funkshun recursion () {coll recursion();}}
                                                 ^
```

<b>Recovery Method:</b>
<ol>
<li>Report the error.</li>
<li>Skip the closing brace and get the next token.</li>
<li>Continue parsing.</li>
</ol>

### 3. Panic Mode Recovery:
Any error that is not handled by the above recovery methods will be handled by panic mode recovery.

<b>Recovery Method:</b>
<ol>
<li>Report syntax error.</li>


<li><code>T</code> is the next token in the input.</li>

```
if nextToken does not exist:
    finish parsing
else: 
    while T is not ';' or '}':
        skip T and get the token after T if exists
```


<li>If parser reaches here, it means that the next token, <code>T</code> is either <code>;</code> or <code>}</code>
<br><code>S</code> is the current top of the stack.
<br><code>pt[S, T]</code> corresponds to the cell in the parse table with <code>S</code> as the top of stack and <code>T</code> as the next token in the input.</li>

```
while S is not 0 and pt[S, T] is not an error:
    pop from stack twice
    if S is 0:
        skip T
    else:
        leave panic mode and continue parsing
```
</ol>


