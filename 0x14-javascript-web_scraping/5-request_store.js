#!/usr/bin/node
const request = require('request');

const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.appendFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
