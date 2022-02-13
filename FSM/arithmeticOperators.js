// fsm-config: {"font" : "Arial"}

// arithmeticOperator ::= "+" | "-" | "*" | "/" | "%"

let arithmeticOperator = {
    initial: 'emptyOperator',
    final: ['plus', 'minus', 'times', 'divide', 'modulo'],
    events: [
        {name: '+', from: 'emptyOperator', to: 'plus'},
        {name: '-', from: 'emptyOperator', to: 'minus'},
        {name: '*', from: 'emptyOperator', to: 'times'},
        {name: '/', from: 'emptyOperator', to: 'divide'},
        {name: '%', from: 'emptyOperator', to: 'modulo'}
    ],
    states: [
        {name: 'emptyOperator'},
        {name: 'plus', color: 'green', shape: 'ellipse'},
        {name: 'minus', color: 'green', shape: 'ellipse'},
        {name: 'times', color: 'green', shape: 'ellipse'},
        {name: 'divide', color: 'green', shape: 'ellipse'},
        {name: 'modulo', color: 'green', shape: 'ellipse'}
    ],
}