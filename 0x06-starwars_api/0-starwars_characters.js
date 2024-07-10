// 0-starwars_characters.js

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from command line argument

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Making a GET request to fetch data about the movie
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetching each character's data
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Failed to retrieve character data. Status:', response.statusCode);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name); // Print each character's name
        }
      });
    });
  }
});
