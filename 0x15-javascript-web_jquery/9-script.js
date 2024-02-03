const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(function () {
  $.get(url, body => {
    $('div#hello').text(body.hello);
  });
});
