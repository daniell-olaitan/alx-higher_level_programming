function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/';

  $.get(url, { lang: $('input#language_code').val() }, body => {
    $('div#hello').text(body.hello);
  });
}

$(function () {
  $('input#btn_translate').click(translate);
  $('input#language_code').focus(() => {
    $(this).keypress((event) => {
      if (event.which === 13) {
        translate();
      }
    });
  });
});
