
<template>
  
  <section id="displayBudgetSectionB">
    <h1>Track Spending</h1>
    
    
    <div class="card">
  <img src="@/assets/budget.jpg" alt="income total"  style="width:100%">
  <div class="container">
    <h1>Total Budget = {{ totals }}</h1>


</div>
</div>
<button @click="trackSpending">Start Tracking </button>
</section>

<div id="alerterror" v-if="message == 'You are off budget manage your expenses now to get you back on track'">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
  {{ message }}
</div>
<div id="alert" v-else-if="message == 'Great You are on budget! Keep up the good work on your personal finance management.'">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
  {{ message }}
</div>
<div id="message2" v-else-if="message == 'You have insufficient funds to spend. Amend budget plan or receive higher income'">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
  {{ message }}
</div>
    <table v-for="(item, i) in $props.ids['datas']" :key="[item.key, i]" class="TrackSpendingTable">
      <tr >
        <th>Spent</th>
        <th>Budget</th>
        <th>{{ datetypes }}</th>
         <th>Expense Name</th>
        <th>Expense Type</th>
       
        
      </tr>
      
      <tr>
        <td v-if="i == 0"><input id="0" ></td>
        <td v-if="i == 1"><input id="1" ></td>
        <td v-if="i == 2"><input id="2" ></td>
        <td v-if="i == 3"><input id="3" ></td>
        <td v-if="i == 4"><input id="4" ></td>
        <td v-if="i == 5"><input id="5" ></td>
        <td v-if="i == 6"><input id="6" ></td>
        <td v-if="i == 7"><input id="7" ></td>
        <td v-if="i == 8"><input id="8" ></td>
        <td v-if="i == 9"><input id="9" ></td>
      <td>{{item.budget}}<br></td>
      <td>{{item["expensemonth"]}}<br></td>
      <td>{{item["expensename"]}}<br></td>
      <td>{{item["expensetype"]}}<br></td>
      
    </tr>
 

  </table>

</template>
   
   <script>
   
   //import router from './../router/index.js'
    
   export default {
     name: 'TrackSpending',
     props:['ids','costsname', 'datetypes', 'incomes', 'totals'],
     data(){
       return {
         firstname: " " ,
         lastname: " ",
         email: " ",
         budgetplans: [],
         budget: null,
         cost1:0.00,
         cost2:0.00,
         cost3:0.00,
         cost4:0.00,
         cost5:0.00,
         cost6:0.00, 
         cost7:0.00,
         cost8:0.00,
         cost9:0.00,
         cost10:0.00,
         id: 0,
         cost: 0.00,
         message:' ',
         totalBudget: " ",
         arrayofCost : [],
         myarray : ["1","2","3","4","5","6","7","8","9","10"]
       }
     },
     methods:{

   trackSpending(){
    
         
         this.cost1 = parseInt(document.getElementById("0").value) 
         this.cost2 = parseInt(document.getElementById("1").value)
         this.cost3 = parseInt(document.getElementById("2").value)
         this.cost4 = parseInt(document.getElementById("3").value) 
         let moneysaved = ( this.cost1 - this.$props.ids["datas"][0]["budget"])
        +(this.cost2 - this.$props.ids["datas"][1]["budget"] ) + 
        (this.cost3 - this.$props.ids["datas"][2]["budget"]) +
        (this.cost4 - this.$props.ids["datas"][3]["budget"])
          this.cost = this.cost2 + this.cost1 + this.cost3 + this.cost4  + this.cost5 + this.cost6 + this.cost7 + this.cost8 + this.cost9 + this.cost10 
         fetch('http://127.0.0.1:5000/track-spending', { method: "POST", headers:{'Content-Type': 'application/json'},
  body:JSON.stringify({"cost" : this.cost2 + this.cost1 + this.cost3 + this.cost4  + this.cost5 + this.cost6 + this.cost7 + this.cost8 + this.cost9 + this.cost10 , "totalbudget" : this.$props.totals, "moneysaved" : moneysaved, "totalincome": this.$props.incomes,"expensemonth" :this.$props.ids["datas"][0]["expensemonth"]
 })})
  .then(response => {
   return  response.json()
  })
  .then(data => {
     console.log(data)
     this.message = data.messages
     
  });
 
 
  
}
   
   
   
    
     }
     
   }
   
   </script>
   
   <style scoped>
   .card{
    width:100%
   }
   nav {
       list-style-type: none;
       margin: 0;
       padding: 0px;
       overflow: hidden;
       background-color: #C8A2C8;
      
     
     }
     .costs{
      height:10rem;
     }

    .TrackSpendingTable, .TrackSpendingTables{
      position: relative;
      left:10rem;
      bottom:30rem;
      width:77rem;
      height:10rem;
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
   
     #alert{
       background-color: green;
       color: black;
       padding: 10rem;
    
     position: relative;
     bottom:30rem;
     }
    #message2{
     background-color: orange;
     color:black;
     padding: 10rem;
     position: relative;
     bottom:30rem;
     
    }
     #alerterror{
       background-color: red;
       color: black;
       padding: 10rem;
  
     position: relative;
     bottom:30rem;
     }
   </style>
   