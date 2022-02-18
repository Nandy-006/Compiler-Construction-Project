import os

#currentPath = os.getcwd()

for testNumber in ['1','2','3','4','5']:
  
    os.system('python3 Parser.py ' + os.path.join('./LexerTests','Test-'+testNumber,'input'+testNumber+'.lwj'))
    
