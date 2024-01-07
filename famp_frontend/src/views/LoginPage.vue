<template>
    
    <main class="registerContent">
        
        <div id="alerterror" style="display:none;">
          <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> Incorrect Password or/and Username;
        </div>

     <img src="@/assets/icons8-login-100.png"/>
     <form id="registration" >
           <input placeholder="First Name" type="text" name="firstname" v-model="firstname" id="first-name"><br/>
         
           <input placeholder="Email" type="email" name="email" v-model="email" id="email" ><br/>
      
        <input id="submit" type="submit" @click="loginUser()" value="Login">
       
     </form>
       
     </main>
   </template>
   
   <script>
   
   import router from './../router'
    
   
   export default {
     name: 'LoginPage',
   
     data(){
       return {
         firstname: " " ,
         lastname: " ",
         email: " ",
         state: "  ",
         layout: "unsuccessful",
         timeout : 0,
         username: localStorage.getItem('user')
       }
     },
     methods:{
     loginUser(){
       const form = document.getElementById("registration");
    
     const formsData = new FormData(form);
   
     fetch('http://localhost:5000/logins', { method: "POST", body:formsData})
     .then(response => response.text())
     .then(data => function () {
        
    if(data == "success")
    {
         sessionStorage.setItem('user', 'Welcome, '  + formsData.get('firstname'))
             console.log(this.layout);
      sessionStorage.setItem('persons', 'Welcome, '  + formsData.get('firstname'))
        sessionStorage.setItem('message', "success")
       
    }
    else if(data == "unsuccessful")
    {
        sessionStorage.setItem('message', ' ')
    }
       
     })
      
     .catch(function (error) {
       console.log(error);
     });
 

   if (sessionStorage.getItem('message') == 'success')
        {
      
       router.push('/my-profile')

    }
    else if(sessionStorage.getItem('message') == ' '){
        router.push('/login')
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
   
     .alert{
       background-color: green;
       color: black
     }
     #alerterror{
       background-color: red;
       color: black;
       
       padding:2rem;
     }
   </style>
   