#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  error && console.log(error); // Print the error if one occurred
  response && console.log('code:', response.statusCode);
});
