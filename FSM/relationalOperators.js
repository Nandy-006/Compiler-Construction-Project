// fsm-config: {"font" : "Arial"}

// relationalOperator ::= ">" | "<" | ">=" | "<=" | "==" | "!="

let myFsm = {
    initial: 'emptyOperator',
    final: ['greaterThan, lessThan, greaterThanOrEqual, lessThanOrEqual, equal, notEqual'],
    events: [
        {name: '>', from: 'emptyOperator', to: 'greaterThan'},
        {name: '<', from: 'emptyOperator', to: 'lessThan'},
        {name: '=', from: 'greaterThan', to: 'greaterThanOrEqual'},
        {name: '=', from: 'lessThan', to: 'lessThanOrEqual'},
        {name: '=', from: 'emptyOperator', to: 'equalHalf'},
        {name: '!', from: 'emptyOperator', to: 'notEqualHalf'},
        {name: '=', from: 'equalHalf', to: 'equal'},
        {name: '=', from: 'notEqualHalf', to: 'notEqual'}
    ],
    states: [
        {name: 'emptyOperator', shape: 'ellipse'},
        {name: 'equalHalf', shape: 'ellipse'},
        {name: 'notEqualHalf', shape: 'ellipse'},
        {name: 'lessThan', color: 'green', shape: 'ellipse'},
        {name: 'greaterThan', color: 'green', shape: 'ellipse'},
        {name: 'lessThanOrEqual', color: 'green', shape: 'ellipse'},
        {name: 'greaterThanOrEqual', color: 'green', shape: 'ellipse'},
        {name: 'equal', color: 'green', shape: 'ellipse'},
        {name: 'notEqual', color: 'green', shape: 'ellipse'}
    ],
}