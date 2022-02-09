// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let Number = {
    initial: 'EmptyLexeme',
    final: 'Number',
    events: [
        {name: '0-9', from: 'EmptyLexeme', to: 'Number'},
        {name: '0-9', from: 'Number', to: 'Number'},
    ], 
    
    // Final state
    states: [
        {name:"Number",color:"green"}
    ]  
}