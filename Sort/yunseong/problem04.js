// 입력받는 로직
const fs = require('fs');
const input = fs.readFileSync('./input/p4.txt').toString().trim();
const inputs = input.split('\n');
const [n, k] = inputs[0].split(' ').map((e) => +e);

let arrA = inputs[1].split(' ').map((e) => +e);
let arrB = inputs[2].split(' ').map((e) => +e);

// 정렬 기준을 나타내는 콜백 (sort에 전달)
const ascending = (a, b) => a - b;
const descending = (a, b) => b - a;

arrA.sort(ascending);
arrB.sort(descending);

let count = 0;
let max = 0;

for (let i = 0; i < k; i++) {
  if (arrA[i] < arrB[i]) {
    [arrB[i], arrA[i]] = [arrA[i], arrB[i]];
  } else break;
}

console.log(arrA.reduce((arr, cur) => arr + cur));
