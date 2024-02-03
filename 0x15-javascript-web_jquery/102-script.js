const url = 'https://www.fourtonfish.com/hellosalut/';

$(function () {
  $('input#btn_translate').bind('click', () => {
    $.get(url, {lang: $('input#language_code').val()}, body => {
      $('div#hello').text(body.hello);
    });
  });
});
