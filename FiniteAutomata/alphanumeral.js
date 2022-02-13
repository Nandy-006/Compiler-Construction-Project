// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let alphaNumeral = {
    initial: 'EmptyLexeme',
    final: 'Alphanumeral',
    events: [
        {name: 'a-z,A-Z,_,0-9', from: 'EmptyLexeme', to: 'Alphanumeral'},
        {name: 'a-z,A-Z,_,0-9', from: 'Alphanumeral', to: 'Alphanumeral'},
    ], 
    
    // Final state
    states: [
        {name:"Alphanumeral",color:"green"}
    ]  
}