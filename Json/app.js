var Happy_Navbar_Scroll = document.getElementById("Happy_Navbar");

$(document).ready(function(){
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if (scroll > 10) {
            Happy_Navbar_Scroll.classList.add("scroll");
        }
   
        else{
            Happy_Navbar_Scroll.classList.remove("scroll");	
        }
    })
  })