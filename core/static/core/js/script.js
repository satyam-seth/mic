$(document).ready(function() {
  var fixHeight = function() {
    $('.navbar-nav').css(
      'max-height',
      document.documentElement.clientHeight - 150
    );
  };
  fixHeight();
  $(window).resize(function() {
    fixHeight();
  });
  $('.navbar .navbar-toggler').on('click', function() {
    fixHeight();
  });
  $('.navbar-toggler, .overlay').on('click', function() {
    $('.mobileMenu, .overlay').toggleClass('open');
  });
});

$(function(){
  // ADD SLIDEDOWN ANIMATION TO DROPDOWN //
  $('.dropdown').on('show.bs.dropdown', function(e){
      $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.dropdown').on('hide.bs.dropdown', function(e){
      e.preventDefault();
      $(this).find('.dropdown-menu').first().stop(true, true).slideUp(400, function(){
          //On Complete, we reset all active dropdown classes and attributes
          //This fixes the visual bug associated with the open class being removed too fast
          $('.dropdown').removeClass('show');
          $('.dropdown-menu').removeClass('show');
          $('.dropdown').find('.dropdown-toggle').attr('aria-expanded','false');
      });
  });
});