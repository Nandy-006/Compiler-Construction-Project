

class Identifier:
    def __init__(self,test_string:str):
        self.firstIsAlphabet = False
        self.testString = test_string
    
    def isAlphabet(self):

      for test_character in self.testString:
          if not (isalpha(test_character) or test_character=="_"):
              return False

      return True
        

    def isNumber(self):
        pass

    def isAlphaNumeral(self):
        pass

    def isIdentifier(self):
        pass



