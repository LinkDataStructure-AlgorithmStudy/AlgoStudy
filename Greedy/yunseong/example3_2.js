// 파일 입력 받기
const fs = require("fs");

const file = process.platform === "linux" ? "/dev/stdin" : "./test.txt";
const input = fs.readFileSync(file).toString().trim().split("\n");
const firstInput = input[0]
  .trim()
  .split(" ")
  .map((e) => +e);
const secondInput = input[1]
  .trim()
  .split(" ")
  .map((e) => +e);
const n = firstInput[0];
const m = firstInput[1];
const k = firstInput[2];

let count = 0; // 더해지는 숫자의 카운트
let answer = 0; // 최대 값
const [...sortedInput] = secondInput;
sortedInput.sort((a, b) => a - b); // 배열 정렬 시키기
let maxNumberIdx = sortedInput.length - 1; // 배열 최대 값을 가지는 인덱스
let secondMaxNumberIdx = sortedInput.length - 2; // 배열 두번째 최대를 가지는 인덱스
let currentIdx = maxNumberIdx;

for (let i = 0; i < m; i++) {
  // 현재 두번째 수고, 카운트 수가 1인 경우
  if (currentIdx === secondMaxNumberIdx && count === 1) {
    currentIdx = maxNumberIdx;
    count = 0;
    // 카운트가 오버된 경우
  } else if (count >= k) {
    currentIdx =
      currentIdx === maxNumberIdx ? secondMaxNumberIdx : maxNumberIdx;
    count = 0;
  }
  answer += sortedInput[currentIdx];
  count++;
}

console.log(answer);
