const list_item = '<li>Item</li>';
const my_list = 'ul.my_list';

$(function () {
  $('div#add_item').bind('click', () => {
    $(my_list).append(list_item);
  });

  $('div#remove_item').bind('click', () => {
    $(my_list + ' li:last').remove();
  });

  $('div#clear_list').bind('click', () => {
    $(my_list).empty();
  });
});
