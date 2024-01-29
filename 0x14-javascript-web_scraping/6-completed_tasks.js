#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    const todos = JSON.parse(body);
    const completedTodos = {};

    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId.toString();
        completedTodos[userId] = completedTodos[userId] !== undefined
          ? completedTodos[userId] + 1
          : 1;
      }
    }

    console.log(completedTodos);
  }
});
