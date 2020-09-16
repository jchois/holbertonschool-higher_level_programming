#!/usr/bin/node

function rFact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * rFact(num - 1);
  }
}

const num = process.argv[2];
console.log(rFact(num));
