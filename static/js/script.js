$(document).ready(function(){
    //Initializes parallax container
    $('.parallax').parallax();
     //Initializes mobile sidenav
    $('.sidenav').sidenav({edge: "right"});
    //Initializes collapsible container
    $('.collapsible').collapsible();
    //Initializes parallax container
    $('.dropdown-trigger').dropdown();
    //Initializes delete modal alerts
    $('.modal').modal();
  });
// Floating Back to Top Button functionality
// This code was found on https://codepen.io/desirecode/pen/MJPJqV

$(document).ready(function(){ 
  $(window).scroll(function(){ 
      if ($(this).scrollTop() > 100) { 
          $('#scroll').fadeIn(); 
      } else { 
          $('#scroll').fadeOut(); 
      } 
  }); 
  $('#scroll').click(function(){ 
      $("html, body").animate({ scrollTop: 0 }, 600); 
      return false; 
  }); 
});

$('.update-link').click(function(e) {
  var form = $(this).prev('.update-form');
  form.submit();
})

