import re

class Constant:
    def __init__(self, testString:str):
        self.integerRegex = r"[+-]?[0-9]+"
        self.floatRegex = r"[+-]?[0-9]+([.][0-9]+)?([Ee][+-]?[0-9]+)?"
        self.testString = testString


    def isStringConst(self):
        if self.testString[0]=="\"" and self.testString[-1] == "\"":
            return True
        
        return False
    
    def isCharConst(self):
        if 2<=len(self.testString)<=3 and self.testString[0]=="\'" and self.testString[-1] == "\'":
            return True
        return False
    
    def isIntegerConst(self):
        return re.fullmatch(self.integerRegex,self.testString) is not None
    
    def isFloatConst(self):
        return re.fullmatch(self.floatRegex,self.testString) is not None

    def isBooleanConst(self):
        return self.testString in ["stonks","not_stonks"]
    
    def isNull(self):
        return self.testString=="null"
    
    def isConstant(self):
        return self.isBooleanConst() or self.isFloatConst() or self.isIntegerConst() or self.isStringConst() or self.isCharConst() or self.isNull()
    
    def isArrayConst(self):
        if self.testString[0] != "[" or self.testString[-1] != "]":
            return False
        elements = self.testString[1:-1].split(",")
        if len(elements) == 1 and elements[0].strip() == '':
            return True
        else:
            for ele in elements:
                temp = self.testString
                self.testString = ele.strip()
                
                if len(self.testString)<1 or not self.isConstant():
                    self.testString = temp
                    return False
        return True


"""AmIConst = Constant("213E+8989")
print("Integer check: ",AmIConst.isIntegerConst())
print("Float check: ",AmIConst.isFloatConst())
print("Char check: ",AmIConst.isCharConst())
print("Boolean check: ",AmIConst.isBooleanConst())
print("String check: ",AmIConst.isStringConst())

AmIArrayConst = Constant("[ ]")
print("Array Check: ", AmIArrayConst.isArrayConst())"""

