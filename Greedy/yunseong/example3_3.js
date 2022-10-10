const fs = require("fs");
const input = fs.readFileSync("./test.txt").toString().trim().split("\n");
const cardGrid = [];

for (let i = 1; i < input.length; i++) {
  cardGrid.push(input[i].split(" ").map((e) => +e));
}

let answer = -1;
cardGrid.forEach((cards) => {
  // 한 열당 계산
  let rowMin = 99999;
  cards.forEach((card) => {
    if (rowMin > card) {
      rowMin = card;
    }
  });
  if (rowMin > answer) {
    answer = rowMin;
  }
});

console.log(answer);
