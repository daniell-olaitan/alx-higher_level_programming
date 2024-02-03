const newElement = '<li>Item</li>';

$('div#add_item')
  .bind('click', event => {
    $('ul.my_list').append(newElement);
  });
