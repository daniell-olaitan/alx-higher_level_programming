#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const keys = Object.keys(dict);

for (let i = 0; i < keys.length; ++i) {
  const key = keys[i];
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
