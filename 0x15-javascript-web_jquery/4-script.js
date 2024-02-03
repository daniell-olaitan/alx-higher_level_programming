$('div#toggle_header')
  .bind('click', event => {
    $('header').toggleClass('red green');
  });
