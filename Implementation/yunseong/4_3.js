const fs = require("fs");
const input = fs.readFileSync("./test.txt").toString().trim().split("");

const dx = [2, 2, -2, -2, 1, -1, 1, -1];
const dy = [1, -1, 1, -1, 2, 2, -2, -2];
const dirLength = dx.length;
const xTable = {
  a: 1,
  b: 2,
  c: 3,
  d: 4,
  e: 5,
  f: 6,
  g: 7,
  h: 8,
};

let count = 0;

const isOutBound = (nextX, nextY) => {
  return nextX < 1 || nextX > 8 || nextY < 1 || nextY > 8;
};

const point = {
  x: xTable[input[0]],
  y: +input[1],
};

for (let i = 0; i < dirLength; i++) {
  const nextX = point.x + dx[i];
  const nextY = point.y + dy[i];
  if (!isOutBound(nextX, nextY)) count++;
}
console.log(count);
