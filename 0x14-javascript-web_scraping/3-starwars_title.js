#!/usr/bin/node
const request = require('request');
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(filmUrl, (error, response, body) => {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
