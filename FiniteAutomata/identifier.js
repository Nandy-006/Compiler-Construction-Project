// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let identifier = {
    initial: 'EmptyLexeme',
    final: 'Identifier',
    events: [
        {name: 'a-z,A-Z,_', from: 'EmptyLexeme', to: 'Identifier'},
        {name: 'a-z,A-Z,_,0-9', from: 'Identifier', to: 'Identifier'},
    ], 
    
    // Final state
    states: [
        {name:"Identifier",color:"green"}
    ]  
}



