// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let integerConstant = {
    initial: 'EmptyLexeme',
    final: 'integerConstant',
    events: [
        {name: 'eps,+,-', from: 'EmptyLexeme', to: 'signOrNoSign'},
        {name: '0-9', from: 'signOrNoSign', to: 'integerConstant'},
        {name: '0-9', from: 'integerConstant', to: 'integerConstant'},
        
    ], 
    
    // Final state
    states: [
        {name:"integerConstant",color:"green"}
    ]  
}