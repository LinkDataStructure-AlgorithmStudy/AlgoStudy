const fs = require("fs");
const input = fs.readFileSync("./test.txt").toString().trim().split(" ");
let n = +input[0];
const k = +input[1];

let count = 0;

while (true) {
  if (n === 1) {
    break;
  }
  if (n % k === 0) {
    n /= k;
  } else {
    n -= 1;
  }
  count++;
}

console.log(count);
