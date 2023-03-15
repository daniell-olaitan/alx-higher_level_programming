#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const keys = Object.values(dict);
const values = Object.keys(dict);

for (let i = 0; i < keys.length; ++i) {
  const key = keys[i];
  const value = values[i];

  if (Object.hasOwn(newDict, key)) {
    newDict[key] = newDict[key].concat([value]);
  } else {
    newDict[key] = [value];
  }
}

console.log(newDict);
