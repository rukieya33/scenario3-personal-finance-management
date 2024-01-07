<template>
  <footer>
   <h4 id="footer">&copy; CopyRight</h4>
   </footer>
     </template>
     
     <script>
     
     
     export default {
       name: 'FooterPage',
       components:{
        
       },
       data(){
         return {
           backendres: " " 
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
      
         }
       }
     }
     </script>
     
     <style>
        #footer{
          background-color: #C8A2C8;
          color:#000000;
          padding:2rem;
          position:relative;
          height:10rem;
  top:20rem;
        }
     </style>
     