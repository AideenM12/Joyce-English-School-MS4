// Remove item and reload on click
//CSRF Token


$('form').submit(function(event) {
console.log(form)

    event.preventDefault()
    const form = event.target
    let formTokenHolder = $(`#item_id${itemId}`);
    let csrfToken = formTokenHolder.data('token');
    var url = `/cart/remove/${form.item_id.value}`;
    var data = {'csrfmiddlewaretoken': form.csrf_token.value, 'item_type': form.item_type.value, 'item_id': form.item_id.value};
    console.log(data)
  
    $.post(url, data)
    
     .done(function() {
       
         location.reload();
     });
  })
 