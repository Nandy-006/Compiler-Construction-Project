

class Identifier:
    def __init__(self,test_string:str):
        self.testString = test_string
    
    def isAlphabet(self):
      # Checks every character in string is alphabet or underscore
      for test_character in self.testString:
        if not (test_character.isalpha() or test_character=="_"):
            return False

      return True
        
    def isNumber(self):
        return self.testString.isnumeric()

    def isAlphaNumeral(self):
        return self.testString.isalnum()
        
    def isIdentifier(self):
        if not self.testString[0].isalpha():
            return False
        
        return self.isAlphaNumeral()
    
        



        


        



