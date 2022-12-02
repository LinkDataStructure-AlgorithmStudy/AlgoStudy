// 입력 로직 선언
const fs = require('fs');
const input = fs.readFileSync('./input/p2.txt').toString().trim();
const [n, ...inputNumbers] = input.split('\n').map((e) => +e);

// 필요한 함수 선언

inputNumbers.sort((a, b) => b - a); // 내림차순 정렬 API

const result = inputNumbers.join(' '); // 결과 배열을 공백으로 구분된 값을 나타내는 문자열로 나타냄. ex) 12 15 27 등등

console.log(result);
