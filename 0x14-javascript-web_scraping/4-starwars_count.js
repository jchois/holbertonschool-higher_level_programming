#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { console.error(error); }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(films => {
    const char = films.characters;
    char.forEach(char => {
      if (char.includes('/18')) {
        count++;
      }
    });
  });
  console.log(count);
});
