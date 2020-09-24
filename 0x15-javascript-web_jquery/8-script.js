$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (resp) {
  resp.results.forEach(function (film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
