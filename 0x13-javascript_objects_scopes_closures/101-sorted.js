#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map(key => {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  } else {
    newDict[dict[key]].push(key);
  }

  return newDict;
});

console.log(newDict);
