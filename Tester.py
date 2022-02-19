# Runs all the test suites sequentially
# Generates individual output files

import os

for index in range(1,11):
    testNumber = str(index)

    testFolderPath = './LexerTests/Test-'+testNumber+"/"
    
    inputPath = testFolderPath + 'input'+testNumber+'.lwj'
    outputPath = testFolderPath + 'output'+testNumber+'.txt'

    os.system('python3 Parser.py ' + inputPath + " > " + outputPath + " 2>&1")