KEYWORDS = [
    "whil", "if", "else", "stonks", "not_stonks", "retun", "intijur", "flote", "bulen",
    "strin", "funkshun", "array", "coll", "null", "let", "char"
]

SYMBOLS = [
    "{", "}", "(", ")", "[", "]", ";", ",", "+", "-", "*", "/", "%"
]

DELIMITERS = [
	"{", "}", "(", ")", "[", "]", ";", ",", "+", "-", "*", "/", "%", 
	">", "<", ">=", "<=", "==", "!=", "=", "||", "&&", "!"
]

TOKENS = {
    "whil": (0, "KEYWD_WHILE"),
  	"if": (1, "KEYWD_IF"),
  	"else": (2, "KEYWD_ELSE"),
  	"stonks": (3, "KEYWD_TRUE"),
  	"not_stonks": (4, "KEYWD_FALSE"),
  	"retun": (5, "KEYWD_RETURN"),
  	"intijur": (6, "KEYWD_INT"),
  	"flote": (7, "KEYWD_FLOAT"),
  	"bulen": (8, "KEYWD_BOOL"),
    "strin": (9, "KEYWD_STRING"),
    "funkshun": (10, "KEYWD_FUNCTION"),
    "array": (11, "KEYWD_ARRAY"),
    "coll": (12,	"KEYWD_CALL"),
    "null": (13,	"KEYWD_NULL"),
    "let": (14, "KEYWD_LET"),
    "char": (15, "KEYWD_CHAR"),
  	"{": (32, "SYM_OP_CURLY"),
  	"}": (33, "SYM_CL_CURLY"),
  	"(": (34, "SYM_OP_PAR"),
  	")": (35, "SYM_CL_PAR"),
  	"[": (36, "SYM_OP_BRACK"),
  	"]": (37, "SYM_CL_BRACK"),
  	";": (38, "SYM_SEMICOLON"),
  	",": (39, "SYM_COMMA"),
  	"+": (40, "SYM_PLUS"),
  	"-": (41, "SYM_MINUS"),
  	"*": (42, "SYM_ASTERISK"),
  	"/": (43, "SYM_SLASH"),
  	"%": (44, "SYM_PERC"),
    ">": (45, "SYM_GT"),
  	"<": (46, "SYM_LT"),
  	">=": (47, "SYM_GTEQ"),
  	"<=": (48, "SYM_LTEQ"),
  	"==": (49, "SYM_ISEQ"),
  	"!=": (50, "SYM_NOTEQ"),
  	"=": (51, "SYM_ASSIGN"),
  	"||": (52, "SYM_OR"),
  	"&&": (53, "SYM_AND"),
  	"!": (54, "SYM_NOT"),
  	"INT": (64, "LITERAL_INT"),
  	"FLOAT": (65, "LITERAL_FLOAT"),
  	"CHAR": (66, "LITERAL_CHAR"),
  	"STRING": (67, "LITERAL_STRING"),
  	"IDENTIFIER": (69, "IDENTIFIER")
}

class STATES:
	EMPTY_LEXEME = "emptyLexeme"
	ALPHABET = "alphabet"
	ALNUM = "alnum"
	NUMBER = "number"
	POINT = "point"
	FLOAT = "float"
	EXPONENT = "exponent"
	EXPONENT_SIGN = "exponentSign"
	OPEN_CHAR = "openChar"
	CHAR = "char"
	OPEN_STRING = "openString"
	GREATER_THAN = "greaterThan"
	LESS_THAN = "lessThan"
	EQUAL_HALF = "equalHalf"
	NOT_EQUAL_HALF = "notEqualHalf"
	OR_HALF = "orHalf"
	AND_HALF = "andHalf"
	