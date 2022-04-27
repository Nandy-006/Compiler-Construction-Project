# Utility class that creates variables for Intermediate Code Generation
class ICVar:
    tcount = 0
    lcount = 0
    
    def __init__(self, temp = None, code = []):
        if temp is not None:
            self.temp = temp
        else:
            ICVar.tcount += 1
            self.temp = f"T{ICVar.tcount}"
        self.code = code
    
    def __str__(self):
        return f"temp: {self.temp}\ncode: {self.code}"
    
    def getNewLabel():
        ICVar.lcount += 1
        return f"L{ICVar.lcount}"
    
def IC_copy(E):
    return ICVar(E.temp, E.code)

def IC_concat(E1, E2):
    return ICVar("", E1.code + E2.code)

# Implements various routines to get intermediate code based on reduction rules. [Check rules.txt for rules corresponding to numbers]
def getICVar(ruleIndex, popped):
    if ruleIndex in [0, 18, 20, 23, 39, 46, 47, 53, 54, 55, 56, 57, 58, 60, 80, 90]:
        return IC_copy(popped[0])
    elif ruleIndex in [1, 4, 59, 67, 68]:
        return ICVar("")
    elif ruleIndex in [2, 3, 89]:
        return IC_concat(popped[0], popped[1])
    elif ruleIndex in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 21, 22, 24, 25, 26, 27, 28, 34, 35, 36, 37, 38, 41, 42, 43, 44, 45]:
        return ICVar(popped[0].temp)
    elif ruleIndex in [16]:
        return ICVar("or")
    elif ruleIndex in [17]:
        return ICVar("and")
    elif ruleIndex in [32]:
        return ICVar(code = popped[1].code + popped[2].code)
    elif ruleIndex in [33]:
        return ICVar(code = popped[1].code)
    elif ruleIndex in [49]:
        return ICVar(code = ICVar(popped[1].temp, popped[1].code))
    elif ruleIndex in [51]:
        res = ICVar()
        res.code = popped[1].code + [("not", popped[1].temp, None, res.temp), ("=", res.temp, None, res.temp)]
        return res
    elif ruleIndex in [52]:
        res = ICVar()
        res.code = popped[1].code + [("minus", popped[1].temp, None, res.temp), ("=", res.temp, None, res.temp)]
        return res
    elif ruleIndex in [61]:
        return ICVar("", popped[2].code + [("=", popped[2].temp, None, popped[0].temp)])
    elif ruleIndex in [62]:
        return ICVar("", popped[0].code + popped[2].code)
    elif ruleIndex in [63]:
        return ICVar("", [("=", popped[2].temp, None, popped[0].temp)] + popped[4].code)
    elif ruleIndex in [65]:
        return ICVar ("", popped[3].code + [("=", popped[3].temp, None, popped[1].temp)])
    elif ruleIndex in [69]:
        L1 = ICVar.getNewLabel()
        L2 = ICVar.getNewLabel()
        return ICVar("", popped[2].code + [
            ("==", popped[2].temp, 0, L1),
            (None, None, None, L2),
            ("LABEL", L1, None, None)
        ] + popped[8].code + [
            ("LABEL", L2, None, None)
        ])
    elif ruleIndex in [70, 71]:
        L1 = ICVar.getNewLabel()
        return ICVar("", popped[2].code + [
            ("==", popped[2].temp, 0, L1)
        ] + popped[5].code + [
            ("LABEL", L1, None, None)
        ])
    elif ruleIndex in [72]:
        L1 = ICVar.getNewLabel()
        L2 = ICVar.getNewLabel()
        return ICVar("", popped[2].code + [
            ("==", popped[2].temp, 0, L1)
        ] + popped[5].code + [
            (None, None, None, L2),
            ("LABEL", L1, None, None)
        ] + popped[9].code + [
            ("LABEL", L2, None, None)
        ])
    elif ruleIndex in [78]:
        res = ICVar()
        res.code = popped[0].code + popped[2].code + [(popped[1].temp, popped[0].temp, popped[2].temp, res.temp)]
        return res
    elif ruleIndex in [79]:
        res = ICVar()
        L1 = ICVar.getNewLabel()
        L2 = ICVar.getNewLabel()
        res.code = popped[0].code + popped[2].code + [
            (popped[1].temp, popped[0].temp, popped[2].temp, L1),
            ("=", 0, None, res.temp),
            (None, None, None, L2),
            ("LABEL", L1, None, None),
            ("=", 1, None, res.temp),
            ("LABEL", L2, None, None)
        ]
        return res
    else:
        return ICVar("", [("Rule not an expression or conditional", None, None, None)])