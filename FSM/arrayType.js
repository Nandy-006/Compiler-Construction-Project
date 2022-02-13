// fsm-config: {"font" : "Arial"}

// arrayType ::= "array" "<" ("intijur" | "flote" | "bulen" | "strin") ">"

let arrayType = {
    initial: 'emptyArrayType',
    final: 'arrayTypeEnd',
    events: [
        {name: 'array', from: 'emptyArrayType', to: 'arrayKeyword'},
        {name: '<', from: 'arrayKeyword', to: 'arrayTypeStart'},
        {name: 'intijur, flote, bulen, strin', from: 'arrayTypeStart', to: 'arrayDataType'},
        {name: '>', from: 'arrayDataType', to: 'arrayTypeEnd'}
    ],
    states: [
        {name: 'emptyArrayType', shape: 'ellipse'},
        {name: 'arrayKeyword', shape: 'ellipse'},
        {name: 'arrayTypeStart', shape: 'ellipse'},
        {name: 'arrayDataType', shape: 'ellipse'},
        {name: 'arrayTypeEnd', color: 'green', shape: 'ellipse'}
    ],
}