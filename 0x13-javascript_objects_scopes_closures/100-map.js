#!/usr/bin/node
const listInput = require('./100-data').list;
const listOutput = [];
listInput.map((elem, i) => {
  listOutput.push(elem * i);
});
console.log(listInput);
console.log(listOutput);
