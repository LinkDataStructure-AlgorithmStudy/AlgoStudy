const fs = require("fs");
const input = fs.readFileSync("./test.txt").toString().trim().split("\n");
const [nm, status, ...gridStr] = input;
const [n, m] = nm.split(" ");
const [charX, charY, look] = status.split(" ").map((e) => +e);
const grid = gridStr.map((row) => row.split(" ").map((e) => +e));

const isVisited = [];
for (let i = 0; i < n; i++) {
  const row = [];
  for (let j = 0; j < m; j++) {
    row.push(0);
  }
  isVisited.push(row);
}

const dx = [0, 1, 0, -1];
const dy = [-1, 0, 1, 0];

const user = {
  x: charX,
  y: charY,
  moveCnt: 0,
  lookDirection: look,
  rotateCnt: 0,
};

const rotateNextDirection = () => {
  user.lookDirection = (user.lookDirection + 3) % 4;
  user.rotateCnt = user.rotateCnt + 1;
};

const isGround = (x, y) => {
  return grid[y][x] === 0;
};

const isOutBound = (x, y) => {
  return x < 0 || x > m - 1 || y < 0 || y > n - 1;
};

if (isGround(user.x, user.y)) {
  user.moveCnt++;
  isVisited[user.y][user.x] = 1;
  rotateNextDirection();
  while (1) {
    if (user.rotateCnt > 3) break;
    const nextX = user.x + dx[user.lookDirection];
    const nextY = user.y + dy[user.lookDirection];
    if (
      !isGround(nextX, nextY) ||
      isOutBound(nextX, nextY) ||
      isVisited[nextY][nextX] === 1
    ) {
      rotateNextDirection();
      continue;
    } else {
      isVisited[nextY][nextX] = 1;
      user.x = nextX;
      user.y = nextY;
      user.moveCnt = user.moveCnt + 1;
      user.rotateCnt = 0;
    }
  }
}

console.log(user.moveCnt);
