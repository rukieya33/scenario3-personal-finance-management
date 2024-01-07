<template>



<router-link to="/dashboard" @click="setcurrenttab" v-if="$props.text != ' '">View Dashboard</router-link> 
<router-link to="/budgets"  v-if="$props.text != ' '">SetBudgets</router-link>
<router-link to="/manage-investment" @click="setcurrenttab"  v-if="$props.text != ' '">Manage Investments</router-link>

<h3 id="personz" > {{ text }}</h3>
       </template>
       
       <script>
      
       
       export default {
         name: 'NavBar2',
         props:['users', 'text'],
         data(){
          return{
            currentstate : 'notactive'
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
       
