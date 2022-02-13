// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let arrayType = {
    initial: 'EmptyLexeme',
    final: 'ArrayType',
    events: [
        {name: 'array', from: 'EmptyLexeme', to: 'arrayStart'},
        {name: '<', from: 'arrayStart', to: 'arrayBegin'},
        {name: 'intijur,flote,bulen,strin', from: 'arrayBegin', to: 'dataType'},
        {name: '>', from: 'dataType', to: 'ArrayType'},
    ], 
    
    // dataType = intijur,flote,bulen,strin
    // Final state
    states: [
        {name:"ArrayType",color:"green"}
    ]  
}