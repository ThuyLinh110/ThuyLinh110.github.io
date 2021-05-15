
$(window).scroll(function() {
    var scrollDistance = $(this).scrollTop();

    $('section').each(function(i) {
            if ($(this).offset().top <= scrollDistance) {
                    $('.navigation a.active').removeClass('active');
                    $('.navigation a').eq(i+1).addClass('active');
            }
    });
}).scroll();


  function menuColor(elmt)

       {    // change color nav
           let titleMenu;
           titleMenu=document.getElementsByClassName("navigation_link");
           for (let i=0;i<titleMenu.length;i++)
           {
              titleMenu[i].style.color="";
              
           }
           elmt.className+='active';
           var x = document.getElementById("naVigation");
           x.className = "navigation";


       }
   
       
        var elements = document.getElementsByClassName("column");      
        var i;
        function two() {
          for (i = 0; i < elements.length; i++) {
            elements[i].style.msFlex = "40%";  
            elements[i].style.flex = "40%";
          }
        }
        
        function four() {
          for (i = 0; i < elements.length; i++) {
            elements[i].style.msFlex = "15%";  
            elements[i].style.flex = "15%";
          }
        }
        
        var header = document.getElementById("myHeader");
        var btns = header.getElementsByClassName("btn-blog");
        for (var i = 0; i < btns.length; i++) {
          btns[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
          });
        }

        function Send()
        {
            document.getElementById("name").value="";
            document.getElementById("email").value="";
            document.getElementById("message").value="";
        }

  function myFunction() {
  var x = document.getElementById("naVigation");
  if (x.className === "navigation") {
    x.className += " responsive";
  } else {
    x.className = "navigation";
  }
}