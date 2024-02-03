const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, body => {
  const results = body.results;
  for (const movie of results) {
    $('<li>').text(movie.title).appendTo($('ul#list_movies'));
  }
});
