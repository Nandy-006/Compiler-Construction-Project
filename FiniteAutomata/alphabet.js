// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let alphabet = {
    initial: 'EmptyLexeme',
    final: 'Alphabet',
    events: [
        {name: 'a-z,A-Z,_', from: 'EmptyLexeme', to: 'Alphabet'},
        {name: 'a-z,A-Z,_', from: 'Alphabet', to: 'Alphabet'},
    ], 
    
    // Final state
    states: [
        {name:"Alphabet",color:"green"}
    ]  
}