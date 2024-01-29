#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
