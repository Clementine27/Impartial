// console.log("greetings, fine shyt"); 

let humanScore = 0;
let computerScore = 0; 

// const humanSelection = getHumanChoice(); 
// const computerSelection = getComputerChoice(); 



/**
 * generate rock, paper, scissors randomly ONCE
 * @returns rock/paper/scissors 
 */
function getComputerChoice(){
    random_no = Math.random(); 
    if (random_no <= 0.3){
        return "rock"; 
    }
    else if (random_no <= 0.6){
        return "scissors";  
    }
    else{
        return "paper"; 
    }
}


/**
 * get user response, normalise then print it 
 * @returns human choice 
 */
function getHumanChoice(){
    return String(prompt("Give me your choice: ")).toLowerCase(); 
    // should print the original 
    // console.log(answer); 
    // return answer; 
}

/**
 * play one round of rock paper scissors where paper < scissors < rock < paper 
 * @param {*} humanChoice 
 * @param {*} computerChoice 
 */
function playRound(humanChoice, computerChoice){
    if (humanChoice == computerChoice){
        console.log("Tie!"); 
    }
    else if ((humanChoice == "paper" && computerChoice == "scissors") || (humanChoice == "scissors" && computerChoice == "rock") || (humanChoice == "rock" && computerChoice == "paper")){
        console.log(`You lost! ${computerChoice} beats ${humanChoice}`); 
        computerScore++; 
    }
    else{
        console.log(`You won! ${humanChoice} beats ${computerChoice}`); 
        humanScore++; 
    }
    
    console.log(`Current score is You --${humanScore} v CS--${computerScore} `); 
}

/**
 * plays the game 5 times
 * each time, have the system ask the user for a new answer and have the computer generate a new answer as well
 * before we re-evaluate 
 * and then 
 */
function playGame(){
    for (i = 0; i <5; i++){
        humanSelection = getHumanChoice(); 
        computerSelection = getComputerChoice(); 


        playRound(humanSelection, computerSelection); 
    }
}


playGame(); 



// array