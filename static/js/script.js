//Hamburger Menu

function hiddenMenu() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

//Homepage

// Back to top button
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// Search bar
//add a y variable to use the block element used in the menu (share parent or grandparent)
function search_major() { 
    console.log("search_major was called")
    let input = document.getElementById('searchbar').value 
    input=input.toLowerCase(); 
    let x = document.getElementsByClassName('majors'); 
      
    for (i = 0; i < x.length; i++) {  
        if (!x[i].innerHTML.toLowerCase().includes(input)) { 
            // x[i] grab parent make == block
            x[i].style.display="none"; 
        } 
        else { 
            x[i].style.display="list-item";                  
        } 
    } 
} 

function search_financial_aid() {
  let input = document.getElementById('searchbar2').value 
  input=input.toLowerCase(); 

  var x = document.getElementById("financial_aid");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

// CAROUSEL Homepage
var slideIndex,slides,dots,captionText;
function initGallery(){
  slideIndex=0;
  slides=document.getElementsByClassName("imageHolder");
  slides[slideIndex].style.opacity=1;
}
initGallery();
