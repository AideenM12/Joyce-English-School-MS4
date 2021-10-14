// Remove item and reload on click

$('form').submit(function(event) {
    event.preventDefault()
    const form = event.target;    
    const url = `/cart/remove/${form.item_id.value}`;
    const data = {
        'csrfmiddlewaretoken': form.csrf_token.value,
        'item_type': form.item_type.value,
        'item_id': form.item_id.value
    };

    $.post(url, data).done(function() {
        location.reload();
    });
});