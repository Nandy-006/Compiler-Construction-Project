// fsm-config: {"font" : "Roboto", "bgColor": "white", "color": "black", "fontColor":"black", "finalShape": "doubleoctagon"}

let Langwej = {
    initial: 'emptyLexeme',
    final: ['_IDENTIFIER', '_INTEGER', '_KEYWORD', '_FLOAT', 'CHAR', 'STRING', 'GTEQ', 'LTEQ', 'ISEQ', 'NOTEQ', '_GT', '_LT', '_NOT', 'SYMBOL', 'OR', 'AND', '_ASSIGN', "SingleComment","MultipleComment"],
    events: [
        { name: 'whitespace', from: 'emptyLexeme', to: 'emptyLexeme' },

        // Single comment
        { name: 'hashtag', from: 'emptyLexeme', to: 'middleSingleComment'},
        { name: 'anything', from: 'middleSingleComment', to: 'middleSingleComment' },
        { name: 'newline', from: 'middleSingleComment', to: 'SingleComment'},

        // Multiple comment
        { name: 'backtick', from: 'emptyLexeme', to: 'middleMultipleComment'},
        { name: 'anything', from: 'middleMultipleComment', to: 'middleMultipleComment' },
        { name: 'backtick', from: 'middleMultipleComment', to: 'MultipleComment'},

        // Keyword and Identifier
        {name: 'a-z,A-Z,_', from: 'emptyLexeme', to: 'alphabet'},
        {name: 'a-z,A-Z,_', from: 'alphabet', to: 'alphabet'},
        {name: '0-9', from: 'alphabet', to: 'alnum'},
        {name: 'a-z,A-Z,_0-9', from: 'alnum', to: 'alnum'},
        {name: 'symbol, whitespace', from: 'alnum', to: '_IDENTIFIER'},
        {name: 'symbol, whitespace', from: 'alphabet', to: '_KEYWORD'},
        {name: '!KEYWORD', from: '_KEYWORD', to: '_IDENTIFIER', color: "green"},

        // Integer
        {name: '0-9', from: 'emptyLexeme', to: 'number'},
        {name: '0-9', from: 'number', to: 'number'},
        {name: 'symbol, whitespace', from: 'number', to: '_INTEGER'},

        // Float
        {name: '.', from: 'number', to: 'point'},
        {name: '0-9', from: 'point', to: 'float'},
        {name: '0-9', from: 'float', to: 'float'},
        {name: 'symbol, whitespace', from: 'float', to: '_FLOAT'},
        {name: 'e,E', from: 'float', to: 'exponent'},
        {name: '0-9', from: 'exponent', to: 'float'},
        {name: '+, -', from: 'exponent', to: 'exponentSign'},
        {name: '0-9', from: 'exponentSign', to: 'float'},

        // Char
        {name: 'singleQuote', from: 'emptyLexeme', to: 'openChar'},
        {name: 'anything', from: 'openChar', to: 'char'},
        {name: 'backslash', from: 'openChar', to: 'slashChar'},
        {name: 'n,t,doubleQuote,r,backslash', from: 'slashChar', to: 'char'},
        {name: 'singleQuote', from: 'char', to: 'CHAR'},
        {name: 'singleQuote', from: 'openChar', to: 'CHAR'},

        // String
        {name: 'doubleQuote', from: 'emptyLexeme', to: 'openString'},
        {name: 'anything', from: 'openString', to: 'openString'},
        {name: 'doubleQuote', from: 'openString', to: 'STRING'},

        // Operators
        {name: '>', from: 'emptyLexeme', to: 'greaterThan'},
        {name: '<', from: 'emptyLexeme', to: 'lessThan'},
        {name: '=', from: 'greaterThan', to: 'GTEQ'},
        {name: '=', from: 'lessThan', to: 'LTEQ'},
        {name: '=', from: 'emptyLexeme', to: 'equalHalf'},
        {name: '!', from: 'emptyLexeme', to: 'notEqualHalf'},
        {name: '=', from: 'equalHalf', to: 'ISEQ'},
        {name: 'anything', from: 'equalHalf', to: '_ASSIGN'},
        {name: '=', from: 'notEqualHalf', to: 'NOTEQ'},
        {name: 'anything', from: 'greaterThan', to: '_GT'},
        {name: 'anything', from: 'lessThan', to: '_LT'},
        {name: 'anything', from: 'notEqualHalf', to: '_NOT'},
        {name: 'symbol', from: 'emptyLexeme', to: 'SYMBOL'},
        {name: '|', from: 'emptyLexeme', to: 'orHalf'},
        {name: '|', from: 'orHalf', to: 'OR'},
        {name: '&', from: 'emptyLexeme', to: 'andHalf'},
        {name: '&', from: 'andHalf', to: 'AND'},
    ],
    states: [
        { name: 'emptyLexeme', color: 'blue'},
        {name: 'SingleComment', color: "green"},
        {name: 'MultipleComment', color: "green"},
        {name: '_IDENTIFIER', color: "green"},
        {name: '_KEYWORD', color: "green"},
        {name: '_INTEGER', color: "green"},
        {name: '_FLOAT', color: "green"},
        {name: 'CHAR', color: "green"},
        {name: 'STRING', color: "green"},
        {name: 'GTEQ', color: "green"},
        {name: 'LTEQ', color: "green"},
        {name: '_GT', color: "green"},
        {name: '_LT', color: "green"},
        {name: 'ISEQ', color: "green"},
        {name: 'NOTEQ', color: "green"},
        {name: '_ASSIGN', color: "green"},
        {name: '_NOT', color: "green"},
        {name: 'SYMBOL', color: "green"},
        {name: 'OR', color: "green"},
        {name: 'AND', color: "green"}
    ],
}