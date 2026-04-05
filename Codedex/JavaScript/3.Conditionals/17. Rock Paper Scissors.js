// Write code below 💖
let player = 0
let playerConverse = " "
//0 to represent "Rock"
//1 to represent "Paper"
//2 to represent "Scissors
let computer = Math.floor(Math.random()*3)
let computerConverse = 0

if(player === 0 ){
    playerConverse = "Rock"
}else if (player === 1){
    playerConverse = "Paper"
}else if (player === 2){
    playerConverse = "Scissors"
}

if(computer === 0 ){
    computerConverse = "Rock"
}else if (computer === 1){
    computerConverse = "Paper"
}else if (computer === 2){
    computerConverse = "Scissors"
}

if((player === 0 && computer === 1)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The computer won!")
}else if((player === 1 && computer === 0)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The player won!")
}else if((player === 0 && computer === 2)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The player won!")
}else if((player === 2 && computer === 0)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The computer won!")
}else if((player === 1 && computer === 2)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The computer won!")
}else if((player === 2 && computer === 1)){
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("The player won!")
}else{
    console.log("Player picked:" + playerConverse)
    console.log("Computer picked:" + computerConverse)
    console.log("")
    console.log("Draw!")
}