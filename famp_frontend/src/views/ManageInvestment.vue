<template>
  <img src="@/assets/income.jpg" alt="income total" style="width:50%">
  <main >
      <section class="sectionA">
        <h1>Stock Selection:</h1>

<button @click="selectStock">Display List Of Stocks</button>
<div v-show="showstock">
<table v-for="(item, i) in this.stocksarray" :key="[item.companyname,i]" class="TrackSpendingTable">
    <tr >
      <th>Company Name</th>
      <th>Company Size</th>
      <th>Quality Rating</th>
       <th>Current Ratio</th>
      <th>Earnings And Dividends</th>
      <th>Financial Leverage</th>
      <th>Select A stock</th>
    </tr>
    
    <tr>
      
    <td id="company">{{item["new_val"]["companyname"]}}<br></td>
    <td>{{item["new_val"]["companysize"]}}<br></td>
    <td>{{item["new_val"]["qualityrating"]}}<br></td>
    <td>{{item["new_val"]["currentratio"]}}<br></td>
    <td>{{item["new_val"]["earningsanddividends"]}}<br></td>
    <td>{{item["new_val"]["financialleverage"]}}<br></td>
    <td v-if="i == 0"><input id="slec" :value ="isselected0" ><input id="0" type="radio"  name="checkboxgroup"></td>
 <td v-if="i == 1"><input id="slec" :value ="isselected0" ><input id="1" type="radio"  name="checkboxgroup"></td>
 <td v-if="i == 2"><input id="slec" :value ="isselected0" ><input id="2" type="radio"  name="checkboxgroup"></td>

  </tr>
</table>
</div>
<div v-show="showstock">
<h1>Asset Allocation:</h1>

<p><label>Age: </label><input v-model="age"></p>
<p><label>Current Assets: </label><input v-model="currentassets"></p>
<p><label>SavingsPerYear: </label><input v-model="savingsperyear"></p>
<p><label>Marginal Tax Rate: </label><input v-model="marginaltaxrate"></p>
<p><label>Income Required: </label><input v-model="incomerequired"></p>
<p><label>Risk Tolerance  (a number 1 - 10): </label><input v-model="risktolerance"></p>
<p><label>Economic Outlook (a number 1 - 10): </label><input v-model="economicoutlook"></p>
</div>
<button id="assetbtn" @click="setAssetAllocation">Submit Asset Allocation</button>


</section>
<section class="sectionB">
    <router-link id="card3" to="/monitor-investment" >

<div id="container3">
  <h1>Monitor Investments</h1>
  
</div>
          </router-link>
<router-link id="card4" to="/financial-statement-analysis">

<div id="container4">
  <h1>View Financial Statement Analysis</h1>

</div>
</router-link>
      </section>
    
    
   </main>
 </template>
 
 <script>

 export default {
   name: 'ManageInvestment',
   data(){
     return {
      currentassets: 0,
      age: 0,
      savingsperyear: 0, 
      marginaltaxrate: 0,
      incomerequired: 0, 
      risktolerance:0, 
      economicoutlook: 0,
      stocksarray: [],
      showstock: false,
      isselected0: "on",
      isselected1: "on1",
      isselected2 : "on2",
      isselected3: "on3",
      companyselected1: "",
        companyselected2: "",
          companyselected3: "",
            companyselected4: "",
              companyselected5: ""
     }
   },
   methods:{
   
  selectStock(){
     
    fetch('http://127.0.0.1:5000/manage_investment', { method: "GET", headers:{'Content-Type': 'application/json'},
})
.then(response => {
 return  response.json()
})
.then(data => {

console.log(data)
   this.showstock = true


    this.stocksarray = data.stocks["changes"]
    this.companyselected2 =  data.stocks["changes"][1]["new_val"]["companyname"]
    this.companyselected1 =  data.stocks["changes"][0]["new_val"]["companyname"]
    this.companyselected3 =  data.stocks["changes"][2]["new_val"]["companyname"]

    console.log(this.companyselected)
  
});
  },
  setAssetAllocation(){
    
if (document.getElementById('0').checked == true)
{
     fetch('http://127.0.0.1:5000/manage_investment', { method: "POST", headers:{'Content-Type': 'application/json'},
 body:JSON.stringify({"currentAssets" : this.currentassets, 
 "age": this.age, "savingsperyear" : this.savingsperyear,
 "marginaltaxrate" : this.marginaltaxrate, "incomerequired" : this.incomerequired, 
 "risktolerance" : this.risktolerance, 
 "economicoutlook": this.economicoutlook, 
 "selectedstock" : this.isselected0,
  "companyselected"  : this.companyselected1

 })
})
 .then(response => {
  return  response.json()
 })
 .then(data => {
 
     console.log(data)
     
     alert(data.m)
     
 });

}
if (document.getElementById('1').checked == true)
{
     fetch('http://127.0.0.1:5000/manage_investment', { method: "POST", headers:{'Content-Type': 'application/json'},
 body:JSON.stringify({"currentAssets" : this.currentassets, 
 "age": this.age, "savingsperyear" : this.savingsperyear,
 "marginaltaxrate" : this.marginaltaxrate, "incomerequired" : this.incomerequired, 
 "risktolerance" : this.risktolerance, 
 "economicoutlook": this.economicoutlook, 
 "selectedstock" : this.isselected0,
  "companyselected"  : this.companyselected2

 })
})
 .then(response => {
  return  response.json()
 })
 .then(data => {
 
     console.log(data)
     
     alert(data.m)
     
 });
}
if (document.getElementById('2').checked == true)
{
     fetch('http://127.0.0.1:5000/manage_investment', { method: "POST", headers:{'Content-Type': 'application/json'},
 body:JSON.stringify({"currentAssets" : this.currentassets, 
 "age": this.age, "savingsperyear" : this.savingsperyear,
 "marginaltaxrate" : this.marginaltaxrate, "incomerequired" : this.incomerequired, 
 "risktolerance" : this.risktolerance, 
 "economicoutlook": this.economicoutlook, 
 "selectedstock" : this.isselected0,
  "companyselected"  : this.companyselected3

 })
})
 .then(response => {
  return  response.json()
 })
 .then(data => {
 
     console.log(data)
     
     alert(data.m)
     
 });
}
  }}
}
 </script>
 
 <style scoped>
 #assetbtn{
  margin:2rem;
 }
 .sectionA, .sectionB{

 
  background-color: gold;
  padding: 2rem;
  width:30vw;
  height:70vh;
  position: relative;
  }
  .sectionA{
      position: relative;
      left:10rem;
      width:40rem;
      height:70rem;
  }
  .sectionB{

      position: relative;
      left:60rem;
      width: 40rem;
      height: 70rem;
      bottom: 70rem;
  }
  
  #container1, #container2, #container3, #container4 {
        background-color: #C8A2C8;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
transition: 0.3s;

        position: relative;
        width: 30rem;
height: 10rem;
     
     
    }
    #card1, #card2, #card3, #card4{
      margin:4rem;
      background-color: #C8A2C8;
box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
transition: 0.3s;
width: 30rem;
height: 10rem;
    }
    #container1:hover, #container2:hover, #container3:hover, #container4:hover{
  
      background-color: black;
box-shadow: white;
transition: 0.3s;
color:white;
width: 30rem;
height: 10rem;
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
     background-color: black;
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
 