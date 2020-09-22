#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { console.error(error); }

  const todos = JSON.parse(body);
  const tasks = {};

  todos.forEach(completed => {
    if (completed.completed === true) {
      const countUser = completed.userId;

      if (countUser in tasks) {
        tasks[countUser]++;
      } else {
        tasks[countUser] = 1;
      }
    }
  });
  console.log(tasks);
});
