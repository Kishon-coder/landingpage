// Getting input via STDIN
const readline = require("readline");

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
  userInput.push(data);
});

inp.on("close", () => {
  let n=userInput[0];

  for(let row=1;row<=n;row++){
    let line=[]

    for(let col=1;col<=row;col++){
        line.push(col);
    }
    console.log(line.join(' '))
  }

});