$(document).ready(function(){
    $('.parallax').parallax();
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.dropdown-trigger').dropdown();
  });

//This code was taken from Code Institutes Boutique Ado Tutorials
  function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 10;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});


$('.update-link').click(function(e) {
  var form = $(this).prev('.update-form');
  form.submit();
})

//M.toast({html: message, displayLength: duration})