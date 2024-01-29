#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    films = JSON.parse(body).results;
    char18 = films.filter(item => {
      return item.characters.find(user => user.endsWith('/18/'));
    });

    console.log(char18.length);
  }
});
