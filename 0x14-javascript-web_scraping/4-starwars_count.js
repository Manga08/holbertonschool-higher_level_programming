#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];
request(URL, function (err, response, body) {
  if (err) throw err;
  let ct = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        ct++;
      }
    }
  }
  console.log(ct);
});
