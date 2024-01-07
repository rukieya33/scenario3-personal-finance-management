<template>

  <div id="message" hidden>
   <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>Thank you for registering !
  </div>
  <main class="registerContent">
   <img src="@/assets/registericon.png"/>
   <form id="registration" >
         <input placeholder="First Name"  autocomplete="d"   type="text" name="firstname" v-model="firstname" id="first-name"><br/>
         <input placeholder="Last Name" autocomplete="d"  type="text" name="lastname" v-model="lastname" id="last-name"><br/>
         <input placeholder="Email" autocomplete="d"  type="email" name="email" v-model="email" id="email" ><br/>
         <input id="submit" type="submit" @click="registerUser" value="Register Me">
     
   </form>
     
   </main>
 </template>
 
 <script>
 
 //import router from './../router/index.js'
  
 
 export default {
   name: 'RegisterPage',
 
   data(){
     return {
       firstname: " " ,
       lastname: " ",
       email: " ",
       currentuser: " ",
       user: localStorage.getItem('first')
     }
   },
   methods:{
   registerUser(){
     let myarray = ["dummy", "dummy", "dummy"];
     const form = document.getElementById("registration");
     const formsData = new FormData(form);
     this.currentuser = formsData.get('email')
     for (var i = 0; i <= myarray.length-1; i++)
     {
         myarray[i] = this.currentuser
     }
   // First, prevent the default form submission behavior
   
   for (var p = 0; p <= myarray.length-1; p++)
     {
         if(myarray[p] == formsData.get('email'))
         {
            alert('You already have an account with us.')
            localStorage.setItem('first', "notnew")
          localStorage.setItem('email', "notnew")
          break;
         }
         else
         {
           sessionStorage.setItem('persons',  ' ') 
 
       
   fetch('http://127.0.0.1:5000/registration', { method: "POST", body:formsData})
   .then(response => {
     
    return  response.text()
   })
   .then(data => {
      if (data == "currentPerson"){
 
       localStorage.setItem('first', "notnew")
          localStorage.setItem('email', "notnew")
          
          
         
     }
     
     
 
   })
   .catch(function (error) {
     console.log(error);
 
   });
   break;
 }
 
 }
   
  if (localStorage.getItem('first') == "notnew" && localStorage.getItem('email') == "notnew"){
   
   sessionStorage.setItem('user', 'Welcome, '  + formsData.get('firstname'))
 
    
  sessionStorage.setItem('persons', 'Welcome, ' + formsData.get('firstname'))
 
 
       this.$router.push('/myprofile')
       location.replace('/myprofile')
       
     }
     else{
       
       this.$router.push('/register')
     }
   
    
     
   }
 
  
   }
   
 }
 
 </script>
 
 <style scoped>
 
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
 