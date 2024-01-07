<template>

  <div id=" home" @click="showSlides">Welcome to Homepage</div>

<p>Change image every 2 seconds:</p>

<div class="mySlides">
  <div class="numbertext">1 / 3</div>
  <img src="@/assets/homebudget.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides">
  <div class="numbertext">2 / 3</div>
  <img src="@/assets/investment.jpg" style="width:100%">
  <div class="text">Caption Two</div>
</div>

<div class="mySlides">
  <div class="numbertext">3 / 3</div>
  <img src="@/assets/stockmarket.jpg" style="width:100%">
  <div class="text">Caption Three</div>

</div>

<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>
{{ show }}
</template>
  
  <script>

  export default {
    name: 'HomePage',
   
    data(){
      return {
        slideIndex : 0,
      
      }
    },
    methods:{
      async getResponse(){
       
  this.backendres = await fetch("http://localhost:3333/")
      .then(function(response) {
      return response.json()
    })
    .then(function(data){
     console.log(data)
     return data.message
    })
    .catch(function() {
      // handle the error
    });
   
      },
      showSlides(){

  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  this.slideIndex++;
  if (this.slideIndex > slides.length) {this.slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[this.slideIndex-1].style.display = "block";  
  dots[this.slideIndex-1].className += " active";
  setTimeout(this.showSlides, 2000); // Change image every 2 seconds
}
    }
    
  }
  


  </script>
  
  <style>
  #home {
    position: relative;
    top:100rem;
  }
  * {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
  </style>
  