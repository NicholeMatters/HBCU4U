//Homepage

// Initialize all elements with carousel class.
  <script>
a = 0;
var move = 255;
var slideNum = document.getElementsByClassName("item").length;

left_button.onclick = function () {
    a = (a - 1) % slideNum; // Move back a slide   
    if( a == -1 ) a = slideNum - 1; // If we move past the first slide, move to the last
    ruller.style.left = (a*move) + 'px';
    console.log(a*move); // Consoles the value we want 
}

right_button.onclick = function () {
    a = (a + 1) % slideNum; // Moves to the next slide, will move to the first when need due to %
    ruller.style.left = (a*move) + 'px';
    console.log(a*move); 
}
    </script>

    