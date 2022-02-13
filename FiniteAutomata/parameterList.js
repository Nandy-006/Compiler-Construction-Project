// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let ParameterList = {
    initial: 'EmptyLexeme',
    final: 'ParameterList',
    events: [
        {name: '(', from: 'EmptyLexeme', to: 'ListBegin'},
        {name: 'intijur,flote,bulen,strin,arrayType', from: 'ListBegin', to: 'DatatypeDone'},
        {name: 'space', from: 'DatatypeDone', to: 'IdentifierFA'}, 
        {name: 'a-z,A-Z,_', from: 'IdentifierFA', to: 'IdentifierDone'},
        {name: 'a-z,A-Z,_,0-9', from: 'IdentifierDone', to: 'IdentifierDone'},
        {name: ',', from: 'IdentifierDone', to: 'ListBegin'} ,
        {name: ')',from: 'ListBegin', to: 'ParameterList'}
    ],
    
    // Final state
    states: [
        {name:"ParameterList",color:"green"}
    ]  
}