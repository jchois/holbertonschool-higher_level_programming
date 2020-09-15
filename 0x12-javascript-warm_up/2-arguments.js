#!/usr/bin/node

const myVar = process.argv.slice(2);

if (myVar.length < 3) {
  console.log('No argument');
} else if (myVar.length === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
