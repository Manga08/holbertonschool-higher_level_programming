#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log('code: %d', res.statusCode);
});
