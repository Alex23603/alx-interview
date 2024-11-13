#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// Base URL for the Star Wars API's films endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the movie endpoint to get character URLs
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch each character's name and display in order
  function fetchCharacter(index) {
    if (index >= characters.length) return;
    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      fetchCharacter(index + 1); // Recursively fetch next character
    });
  }

  // Start fetching characters in order
  fetchCharacter(0);
});
