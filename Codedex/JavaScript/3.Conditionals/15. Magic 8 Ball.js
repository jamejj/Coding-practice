// Write code below 💖
let res = Math.floor(Math.random()*10)
let question = "Is Codédex better than Udemy yet?"
let answer = " "

if(res === 0){
    answer = "Yes - definitely."
}else if (res === 1) {
    answer = "It is decidedly so."
}else if (res === 2) {
    answer = "Without a doubt."
}else if (res === 3) {
    answer = "Reply hazy, try again."
}else if (res === 4) {
    answer = "Ask again later."
}else if (res === 5) {
    answer = "Better not tell you now."
}else if (res === 6) {
    answer = "My sources say no."
}else if (res === 7) {
    answer = "My sources say no."
}else if (res === 8) {
    answer = "Outlook not so good."
}else{
    answer = "Very doubtful."
}

console.log("Question: " + question)
console.log("Magic 8 Ball: " + answer)