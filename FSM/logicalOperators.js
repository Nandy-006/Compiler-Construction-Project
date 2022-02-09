// fsm-config: {"font" : "Arial"}

// logicalOperator ::= "||" | "&&"

let myFsm = {
    initial: 'emptyOperator',
    final: 'orOperator, andOperator',
    events: [
        {name: '|', from: 'emptyOperator', to: 'orOperatorHalf'},
        {name: '&', from: 'emptyOperator', to: 'andOperatorHalf'},
        {name: '|', from: 'orOperatorHalf', to: 'orOperator'},
        {name: '&', from: 'andOperatorHalf', to: 'andOperator'}
    ],
    states: [
        {name: 'emptyOperator', shape: 'ellipse'},
        {name: 'orOperator', color: 'green', shape: 'ellipse'},
        {name: 'andOperator', color: 'green', shape: 'ellipse'},
        {name: 'orOperatorHalf', shape: 'ellipse'},
        {name: 'andOperatorHalf', shape: 'ellipse'}
    ],
}