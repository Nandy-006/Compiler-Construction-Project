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

### Running the compiler:

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

### Running Tests:

```bash
python3 Tester.py
```
