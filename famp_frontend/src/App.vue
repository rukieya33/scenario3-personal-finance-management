<template>
  <header>
 <NavBar user="current"></NavBar>
</header>
<main>
  <router-view/>
</main>
  <footer>
     &copy;
  </footer>
 
</template>
<script>
import NavBar from './views/NavBar.vue';


export default {
    
    data() {
        return {
            person: " ",
            username: " "
        };
    
    },
    components: { NavBar }
}

</script>
<style>
header{
position:relative;
bottom:3rem;
background-color:gold;
padding: 3rem;
}
nav {
    list-style-type: none;
    margin: 0;
    width: 100%;
    padding: 0px;
    overflow: hidden;
    background-color: #C8A2C8;
    height: 2.8rem;
  
  }
 .contents button :not(:hover){
    background-color:#C8A2C8 ;
    width: 10rem;
    height:5rem;
    margin: 2rem;
 }
 #previousbtn:not(:hover){
  background-color:#C8A2C8 ;
  width: 10rem;
  height:3rem;
  margin: 1rem;
  position: relative;
  bottom:30rem;
  left:2rem;
  font-size: medium;
  border-radius: 0.2rem;
 }
 #previousbtn2:not(:hover){
  background-color:#C8A2C8 ;
  width: 10rem;
  height:3rem;
  margin: 1rem;
  position: relative;
  bottom:34rem;
  left:2rem;
  font-size: medium;
  border-radius: 0.2rem;
 }
 #previousbtn2:hover{
  background-color: #111;
  color:white;
  width: 10rem;
  height:3rem;
  margin: 1rem;
  position: relative;
  bottom:34rem;
  left:2rem;
  font-size: medium;
  border-radius: 0.2rem;
 }
 #previousbtn:hover{
  background-color: #111;
  color:white;
  width: 10rem;
  height:3rem;
  margin: 1rem;
  position: relative;
  bottom:30rem;
  left:2rem;
  font-size: medium;
  border-radius: 0.2rem;
 }
 #nextbtn{
  position: relative;
  top:12rem;
 }
 #personz{
  position:relative;
  bottom: 0.5rem;
 }
   a {
    display: block;
    color: black;
    border-color: white;
    border-style:solid ;
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
 
footer{
    padding: 5rem;
    background-color:khaki;
    position: relative;
    top: 10rem;
}

</style>
