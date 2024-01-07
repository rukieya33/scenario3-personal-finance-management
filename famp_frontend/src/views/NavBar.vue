<template>
 
<nav id="navs">
    <router-link to="/" @click="showSlides">Home</router-link> 
    <router-link to="/register" v-if="p == null">Register</router-link>
   
    <Navbar2  v-bind:text="p" v-bind:users="current" v-else></Navbar2>
   
   
  </nav>

   </template>
   
   <script>
   
   //import router from './../router/index.js'
    import Navbar2 from './Navbar2.vue'
   
   export default {
     name: 'NavBar',
     props:['user'],
     
     components:{Navbar2},
     data(){
       return {
    
         firstname: " " ,
         lastname: " ",
         email: " ",
         current: "iscurrent",
         notperson: 'notcurrent',
         p: sessionStorage.getItem('persons')
       }
     
     },
     methods:{
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
   
   <style scoped>
   #navs .active-tab{
    background-color: #111;
    color:white;
   }
   .registerContent{
     position: relative;
     top:1rem;
     background-image: url('./../assets/graphic-1714230.svg');
     height:33rem;
   
   }
   #registration{
     position: relative;
     top:2rem;
   }
   #registration #submit{
     position: relative;
     left:0.1rem;
   }
   #registration #submit:not(:hover)
   {
     background-color:#0000ff;
     color:#ffffff;
   }
   #registration #submit:hover
   {
     background-color:#000000;
     color:white
   }
   #registration a{
     position: relative;
     top:3rem;
     left:58rem;
   }
   #registration input, button{
     border-radius: 0.5rem;
     width: 20rem;
     height:2rem;
     margin:1rem;
   }
   nav {
       list-style-type: none;
       margin: 0;
       padding: 0px;
       overflow: hidden;
       background-color: #C8A2C8;
      
     
     }
    
      a {
       display: block;
       color: rosebrown;
       
       text-decoration: none;
   
       float: left;
       padding: 14px 16px;
     }
     
     /* Change the link color to #111 (black) on hover */
    a:hover {
       background-color: #111;
       color:white;
     }
    a:not(:hover) {
       background-color:#C8A2C8;
     }
   
     #message{
       background-color: green;
       color: black
     }
    #message2{
     background-color: orange;
     color:black;
    }
     .alerterror{
       background-color: red;
       color: black
     }
   </style>
   