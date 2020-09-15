#!/usr/bin/node

const size = process.argv[2];

if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else if (isNaN(size) || size === undefined) {
  console.log('Missing size');
}
