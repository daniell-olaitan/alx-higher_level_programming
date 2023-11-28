#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

const func = function (key) {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
};

for (const key of Object.keys(dict)) {
  func(key);
}

console.log(newDict);
