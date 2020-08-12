// // FILTER IMPORTS
// import React from "react";
// import ReactDOM from "react-dom";
// import App from "./App";
// import registerServiceWorker from "./registerServiceWorker";
// import { createStore, compose, applyMiddleware, combineReducers } from "redux";
// import { Provider } from "react-redux";
// import thunk from "redux-thunk";

// import authReducer from "./store/reducers/auth";


//Hamburger Menu
function hiddenMenu() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display="none";
  } else {
    x.style.display="block";
  }
}

// Back to top button
mybutton = document.getElementById("myBtn");

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display="block";
  } else {
    mybutton.style.display="none";
  }
}
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};


// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// Search bar
//add a y variable to use the block element used in the menu (share parent or grandparent)
function search_major() { 
    // console.log("search_major was called")
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
    x.style.display="block";
  } else {
    x.style.display="none";
  }
}

// CAROUSEL Homepage
var slideIndex,slides,dots,captionText;
function initGallery(){
  slideIndex=0;
  slides=document.getElementsByClassName("imageHolder");
  slides[slideIndex].style.opacity=1;

  captionText=document.querySelector(".captionHolder .captionText");
  captionText.innerText=slides[slideIndex].querySelector(".captionText").innerText;


  dots=[];
  var dotsContainer=document.getElementById("dotsContainer");

  //will filter throught he loop to connect dots to each picture
  for(var i=0; i<slides.length; i++) {
      var dot=document.createElement("span");
      dot.classList.add("dots");
      dot.setAttribute("onClick","moveSlide("+i+")"); //actives the bottom buttons
      dotsContainer.append(dot);
      dots.push(dot);
  } 
  dots[slideIndex].classList.add("active");
}
initGallery();

function plusSlides(n) {
    moveSlide(slideIndex+n);
}

function moveSlide(n) {
    var i,current,next;
    var moveSlideAnimClass= { //moving slide with CS not JS 
        forCurrent:"",
        forNext:""
    }
    var slideTextAnimClass;
    if(n>slideIndex) {
        if(n>=slides.length) {n=0} //>= allows it to return to the first slide at the end
        moveSlideAnimClass.forCurrent="moveLeftCurrentSlide";
        moveSlideAnimClass.forNext="moveLeftNextSlide";
        slideTextAnimClass="slideTextFromTop";
    }else if (n<slideIndex) {
        if (n<0) {n=slides.length-1}
        moveSlideAnimClass.forCurrent="moveRightCurrentSlide";
        moveSlideAnimClass.forNext="moveRightNextSlide";
        slideTextAnimClass="slideTextFromBottom";
    }
    if (n!=slideIndex) {
        next=slides[n];
        current=slides[slideIndex];
        for (i=0;i<slides.length;i++) {
            slides[i].className="imageHolder";
            slides[i].style.opacity=0;
            dots[i].classList.remove("active");
        }
        current.classList.add(moveSlideAnimClass.forCurrent);
        next.classList.add(moveSlideAnimClass.forNext);
        dots[n].classList.add("active");
        slideIndex=n;

    }
    captionText.style.display="none";
    captionText.className="captionText "+slideTextAnimClass;
    captionText.innerText=slides[n].querySelector(".captionText").innerText;
    captionText.style.display="block";
}

// makes slideshow automatic
var timer=null;
function setTimer() {
    timer=setInterval (function () {
        plusSlides(1);
    },3000)
}
setTimer();

// function playPauseSlides() {
//     var playPauseBtn=document.getElementById("playPauseBtn");
//     if (timer==null) {
//           setTimer();
//           playPauseBtn.style.backgroundPositionY="0px";
//     }else{
//           clearInterval (timer);
//           timer=null;
//           playPauseBtn.style.backgroundPositionY="-33px";
//     }


//Graduate Page read more
function readMore() {
  var cont = document.getElementById("cont");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("newBtn");

  if (cont.style.display === "none") {
    cont.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    cont.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}

// filter

// const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

// const rootReducer = combineReducers({
//   auth: authReducer
// });

// const store = createStore(rootReducer, composeEnhances(applyMiddleware(thunk)));

// const app = (
//   <Provider store={store}>
//     <App />
//   </Provider>
// );

// ReactDOM.render(app, document.getElementById("root"));
// registerServiceWorker();