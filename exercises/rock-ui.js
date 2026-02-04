// initialise buttons 
const rock = document.querySelector("#rock"); 
const paper = document.querySelector("#paper"); 
const scissors = document.querySelector("#scissors"); 
const buttons = document.querySelectorAll(".buttons"); 
const resultsPanel = document.querySelector(".parent-node")

// keep scores 
let humanScore = 0;
let computerScore = 0; 



/**
 * attach listeners and trigger a round 
 */
buttons.forEach((button) => {
    button.addEventListener("click", ()=>{
        let humanSelection = button.textContent; 
        displayResults(humanSelection); 
        playRound(humanSelection, getComputerChoice()); 
        results = ascertainWinner(); 
        displayResults(results); 
    })
    }); 


/**
 * given string, display it on screen 
 * @param string the string that we want to display
 */

function displayResults(string){
    container = document.createElement("div"); 
    container.style.color = "blue"; 
    container.textContent = string; 
    resultsPanel.appendChild(container)
}


/**
 * returns the name of the winner in a game of 
 * rock paper scissors 
 */
function ascertainWinner(){
    // as long as one of the players havent exceeded 5 scores 
    // we continue the game
    if (humanScore == computerScore == 5){
        humanScore = 0; 
        computerScore = 0; 
        return "it's a tie!"; 
    }
    if (humanScore == 5){
        humanScore = 0; 
        computerScore = 0; 
        return "you won the game!"; 
    }
    if (computerScore == 5){
        humanScore = 0; 
        computerScore = 0; 
        return "you lost the game :("; 
    }

}

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
        displayResults("Tie!"); 
    }
    else if ((humanChoice == "paper" && computerChoice == "scissors") || (humanChoice == "scissors" && computerChoice == "rock") || (humanChoice == "rock" && computerChoice == "paper")){
        displayResults(`You lost! ${computerChoice} beats ${humanChoice}`); 
        computerScore++; 
    }
    else{
        displayResults(`You won! ${humanChoice} beats ${computerChoice}`); 
        humanScore++; 
    }
    
    displayResults(`Current score is You --${humanScore} v CS--${computerScore} `); 
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


// playGame(); 



// array