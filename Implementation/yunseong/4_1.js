// 4.1
// time complexity : O(n)
// input file logic
const fs = require("fs");
const input = fs.readFileSync("./test.txt").toString().trim().split("\n");
const n = +input[0];
const direction = input[1].trim().split(" ");

const dx = [-1, 1, 0, 0]; // direction x
const dy = [0, 0, 1, -1]; // direction y
// indicate based by input sign
const dir = {
  U: 0,
  D: 1,
  R: 2,
  L: 3,
};

// start point (1,1)
let point = {
  x: 1,
  y: 1,
};

// check next point is out of range
const isOutBound = (nextX, nextY) => {
  return nextX < 1 || nextX > n || nextY < 1 || nextY > n;
};

// iterate input direction
direction.forEach((arrow) => {
  const nextX = point.x + dx[dir[arrow]];
  const nextY = point.y + dy[dir[arrow]];
  if (!isOutBound(nextX, nextY)) {
    point.x = nextX;
    point.y = nextY;
  }
});

console.log(`${point.x} ${point.y}`);
