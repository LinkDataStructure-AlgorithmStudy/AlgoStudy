// 입력받는 로직
const fs = require('fs');
const input = fs.readFileSync('./input/p3.txt').toString().trim();
const [i_n, ...i_arr] = input.split('\n');
const n = +i_n;

let students = [];

class Student {
  constructor(name, grade) {
    this.name = name;
    this.grade = grade;
  }
}

// 입력 받은 학생들 객체를 만들어 주는 로직
i_arr.forEach((element) => {
  const [name, grade] = element.split(' ');
  students.push(new Student(name, +grade));
});

students.sort((a, b) => a.grade - b.grade);

const result = students.map((student) => student.name).join(' ');

console.log(result);
