const fs = require("fs");
const input = +fs.readFileSync("./test.txt").toString().trim();

let count = 0;
// hour
for (let i = 0; i <= input; i++) {
  if ((i + "").split("").includes("3")) {
    count += 60 * 60;
    continue;
  }
  for (let j = 0; j < 60; j++) {
    if ((j + "").split("").includes("3")) {
      count += 60;
      continue;
    }
    for (let k = 0; k < 60; k++) {
      const time = "" + k;
      if (time.split("").includes("3")) count++;
    }
  }
}

console.log(count);
