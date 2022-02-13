// fsm-config: {"font" : "Arial"}

// arithmeticOperator ::= "+" | "-" | "*" | "/" | "%"
// relationalOperator ::= ">" | "<" | ">=" | "<=" | "==" | "!="
// logicalOperator ::= "||" | "&&" 
// operator ::= arithmeticOperator | relationalOperator | logicalOperator

let operator = {
    initial: 'emptyOperator',
    final: 'operator',
    events: [
        {name: 'arithmeticOperator, relationalOperator, logicalOperator', from: 'emptyOperator', to: 'operator'},
    ],
    states: [
        {name: 'emptyOperator', shape: 'ellipse'},
        {name: 'operator', shape: 'ellipse', color: "green"},
    ],
}