// fsm-config: {"font" : "Arial"}
// fsm-config: {"nodeShape" : "diamond"}
// fsm-config: {"initialShape" : "component", "finalShape" : "tab"}

let floatConstant = {
    initial: 'EmptyLexeme',
    final: 'floatConstant',
    events: [
        {name: 'eps,+,-', from: 'EmptyLexeme', to: 'signOrNoSign'},
        {name: '0-9', from: 'signOrNoSign', to: 'integerPart'},

        {name: '0-9', from: 'integerPart', to: 'integerPart'},
        {name: '.', from: 'integerPart', to: 'floatConstant'},

        {name: '0-9,eps', from: 'floatConstant', to: 'floatConstant'},
        

        {name: 'E,e', from: 'floatConstant', to: 'exponentPart'},
        {name: '+,-', from: 'exponentPart', to: 'signedExponent'},
        {name: '0-9', from: 'exponentPart', to: 'floatConstant'},
        
        {name: '0-9', from: 'signedExponent', to: 'floatConstant'},

        
    ], 

    // No e,E - 4.27
    // With e,E - 1.23e+27
    // 3.45e-55
    
    // Final state
    states: [
        {name:"floatConstant",color:"green"}
    ]  
}