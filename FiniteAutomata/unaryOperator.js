// fsm-config: {"font" : "Arial"}

// unaryOperator ::= "-" | "!"

let unaryOperator = {
    initial: 'emptyOperator',
    final: 'unaryOperator',
    events: [
        { name: '-, !', from: 'emptyOperator', to: 'unaryOperator' },
    ],
    states: [
        { name: 'unaryOperator', color: 'green'},
    ],
}