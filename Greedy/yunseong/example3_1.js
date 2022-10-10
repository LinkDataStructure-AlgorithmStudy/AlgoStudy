let n = 1010;
const coinTypes = [500, 100, 50, 10];
let count = 0;
let idx = 0;

while (n > 0) {
  if (coinTypes[idx] <= n) {
    n -= coinTypes[idx];
    count++;
  } else {
    idx++;
  }
}
console.log(count);
