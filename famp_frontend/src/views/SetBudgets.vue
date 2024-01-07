<template>

  
  <section id="setBudgetSectionA" >
  
     <h1>Income After-Tax Info</h1>
     <label>Weekly Salary</label><input type="radio" name="radiogrup" >
      <label>Monthly Salary</label><input type="radio" name="radiogrup">
     <h3>How many Jobs do you do ?</h3>
     <input class="numberOfJobs" name="numberOfJobs" @input="displayJobs" v-model="number" type="telephone" placeholder="enter a number">
     
     <div id="jobs">
      

     </div>
     
     <button id="calbtn" @click="totalIncome">Calculate Total Income</button>
     
    </section>


 <section  id="setBudgetSectionC" v-if="displaysectionB">
     <h1>Set {{ datetype }}ly Budget Plan</h1>

  
  <table class="BudgetTable">
    <tr >
      <th>Budget</th>
      <th>Expense Type</th>
      <th>Expense Name</th>
      <th>{{ datetype }}</th>
    </tr>
  
    <tr>
    <td><input name="budget1" type="text" v-model="budget" id="budget" placeholder="enter budget value for expense"><br></td>
    <td><input name="budget2" type="text" v-model="expensetype" id="expensetype" placeholder="enter expense type"><br></td>
    <td><input name="budget3"  type="text" v-model="expense1" id="expensename" placeholder="enter expense name"><br></td>
    <td><input name="budget4"  type="text" v-model="expensemonth" id="expensemonth" placeholder="enter expense month"><br></td>
   
  </tr>

  </table>

    <button @click="removeExpense">Remove Expense</button>

    <button id="calbtn" @click="setBudget">Set Budget</button>
 </section>
<section id="displayBudgetSectionA" v-if="!displaysectionB">
 
  <div class="card" >
<img src="@/assets/income.jpg" alt="income total" style="width:100%">
<div class="container">
  <h1>Total Income After-Tax = 0.00</h1>

</div>
</div>
</section>
<section id="displayBudgetSectionC" v-if="displaysectionB">
  <h1> Income After-Tax </h1>
  <div class="card" id="income">
<img src="@/assets/income.jpg" alt="income total" style="width:100%">
<div class="container">
  <h1>Total Income After-Tax = {{ income }}</h1>

</div>
</div>
  </section>
  <button id="previousbtn" @click="state2 = changeToPreviousContent(state2)" v-show="displaysectionB ">Previous</button>
<button id="previousbtn2" @click="state = changeToNextContent(state)" v-if="!displaysectionB">Next</button>


<track-spending v-bind:costsname="nameofCost"  v-bind:ids="id" v-bind:totals="totalBudget" v-bind:datetypes="datetype" v-bind:incomes="income" v-if="displaysectionB"></track-spending>



</template>
<script>
import TrackSpending from './TrackSpending.vue'


 
export default {
  name: 'SetBudget',
  components: {TrackSpending },
  
  data(){
    return {
      datetype: "month",
      childA: true,
      childC: null,
      childB: null,
      displaysectionB: null,
      displaysectionC: true,
      state: -1,
      state2: -1,
      income: 0.00,
      job1: "",
      job2: "",
      job3: "",
      expenseNames: [],
      expense1: " ",
      expensecost: " ",
      expensemonth: " ", 
      expensetype: " ",
      budget: " ",
      totalBudget: 0,
      id: "",
      nameofCost : ""
   
    }
  },
  methods:{


   
    removeExpense(){
   
this.budget = ' '
this.expense1 = ' '
this.expensemonth = ' '
this.expensetype = ' '

    },
    setBudget(){
      this.displaysectionC = false;

   
document.getElementById('displayBudgetSectionC').style.position = ' '
document.getElementById('displayBudgetSectionC').style.bottom = ' '

document.getElementById('displayBudgetSectionB').style.position = '' 
this.totalBudget = this.totalBudget + parseInt(this.budget)

this.expenseNames.push({'income': this.income, 'budget':this.budget, 'expensetype': this.expensetype, 
'expensename' : this.expense1,
'expensemonth' : this.expensemonth })
let myarray = []
this.nameOfCost = myarray.push("cost"+String(this.expenseNames.length))
fetch('http://127.0.0.1:5000/setBudget', { method: "POST", headers:{'Content-Type': 'application/json'},
body:JSON.stringify({"data" : this.expenseNames})})
.then(response => {
 return  response.json()
})
.then(data => {
   console.log(data)
   this.id = data.id['changes'][0]['new_val']
  
   console.log(this.id)
   

});



    
    },
     displayJobs(){
        if(this.number == 1 && document.getElementsByName('radiogrup')[0].checked == true )
        {
           document.getElementById('jobs').innerHTML = '<h3>What is the job role ?</h3> <input type="text" name="names"  placeholder="enter job " class="numberOfJobs"> <h3>What is the monthly or weekly income ? </h3><input type="text" placeholder="enter income in numbers" v-model="income" id="numberOfJobs1" class="numberOfJobs">'
           this.datetype = "Week"
        }
        else if(this.number == 2 && document.getElementsByName('radiogrup')[0].checked == true )
        {
          document.getElementById('jobs').innerHTML = '<h3>What are the job roles ?</h3> <input type="text" name="names" placeholder="enter job 1" class="numberOfJobs"> <input type="text" name="names" placeholder="enter job 2" class="numberOfJobs"><h3>What is the monthly or weekly income of job 1 ? </h3><input type="text" placeholder="enter income in numbers" class="numberOfJobs" id="numberOfJobs2"> <h3>What is the monthly or weekly income of job 2 ? </h3><input type="text" placeholder="enter income in numbers"  class="numberOfJobs" id="numberOfJobs3">'
          this.datetype = "Week"
        }
        else if(this.number == 3 && document.getElementsByName('radiogrup')[0].checked == true )
        {
          document.getElementById('jobs').innerHTML = '<h3>What are the job roles ?</h3> <input type="text"   placeholder="enter job 1" class="numberOfJobs"> input type="text" name="names" placeholder="enter job 1" class="numberOfJobs"> <h3>What is the monthly or weekly income of job 1? </h3><input type="text" placeholder="enter income in numbers"   class="numberOfJobs" id="numberOfJobs4"> <h3>What is the monthly or weekly income of job 2? </h3><input type="text" placeholder="enter income in numbers" class="numberOfJobs" id="numberOfJobs5"><input type="text" placeholder="enter job 3" name="names" class="numberOfJobs"> <h3>What is the monthly or weekly income of job 3 ? </h3><input type="text"  placeholder="enter income in numbers"  class="numberOfJobs" id="numberOfJobs6">'
          this.datetype = "Week"
        }

        if(this.number == 1 && document.getElementsByName('radiogrup')[1].checked == true )
        {
           document.getElementById('jobs').innerHTML = '<h3>What is the job role ?</h3> <input type="text" name="names"  placeholder="enter job " class="numberOfJobs"> <h3>What is the monthly or weekly income ? </h3><input type="text" placeholder="enter income in numbers" v-model="income" id="numberOfJobs1" class="numberOfJobs">'
           this.datetype = "Month"
        }
        else if(this.number == 2 && document.getElementsByName('radiogrup')[1].checked == true )
        {
          document.getElementById('jobs').innerHTML = '<h3>What are the job roles ?</h3> <input type="text" name="names" placeholder="enter job 1" class="numberOfJobs"> <input type="text" name="names" placeholder="enter job 2" class="numberOfJobs"><h3>What is the monthly or weekly income of job 1 ? </h3><input type="text" placeholder="enter income in numbers" class="numberOfJobs" id="numberOfJobs2"> <h3>What is the monthly or weekly income of job 2 ? </h3><input type="text" placeholder="enter income in numbers"  class="numberOfJobs" id="numberOfJobs3">'
          this.datetype = "Month"
        }
        else if(this.number == 3 && document.getElementsByName('radiogrup')[1].checked == true )
        {
          document.getElementById('jobs').innerHTML = '<h3>What are the job roles ?</h3> <input type="text"   placeholder="enter job 1" class="numberOfJobs"> input type="text" name="names" placeholder="enter job 1" class="numberOfJobs"> <h3>What is the monthly or weekly income of job 1? </h3><input type="text" placeholder="enter income in numbers"   class="numberOfJobs" id="numberOfJobs4"> <h3>What is the monthly or weekly income of job 2? </h3><input type="text" placeholder="enter income in numbers" class="numberOfJobs" id="numberOfJobs5"><input type="text" placeholder="enter job 3" name="names" class="numberOfJobs"> <h3>What is the monthly or weekly income of job 3 ? </h3><input type="text"  placeholder="enter income in numbers"  class="numberOfJobs" id="numberOfJobs6">'
          this.datetype = "Month"
        }
    },
    totalIncome(){
        if(this.number == 1)
        {
          document.getElementsByClassName('container')[0].innerHTML = `<h1>Total Income After-Tax = £${document.getElementById('numberOfJobs1').value}, For job(s):</h1><h1>${document.getElementsByName('names')[0].value}</h1>`
          this.income = document.getElementById('numberOfJobs1').value
          
        }
        else if (this.number == 2)
        {
          document.getElementsByClassName('container')[0].innerHTML = `<h1>Total Income After-Tax = £${String(parseInt(document.getElementById('numberOfJobs2').value) + parseInt(document.getElementById('numberOfJobs3').value))}, For job(s):</h1><h1>${document.getElementsByName('names')[0].value} and ${document.getElementsByName('names')[1].value}</h1>`
          this.income = parseInt(document.getElementById('numberOfJobs2').value) + parseInt(document.getElementById('numberOfJobs3').value)
        }
        else if (this.number == 3)
        {
          document.getElementsByClassName('container')[0].innerHTML = `<h1>Total Income After-Tax = £${String(parseInt(document.getElementById('numberOfJobs4').value + document.getElementById('numberOfJobs5').value + document.getElementById('numberOfJobs6')))}, For job(s):</h1><h1>${document.getElementsByName('names')[0].value}</h1>, <h1>${document.getElementsByName('names')[1].value}</h1>,and <h1>${document.getElementsByName('names')[2].value}</h1>`
          this.income = parseInt(document.getElementById('numberOfJobs4').value) + parseInt(document.getElementById('numberOfJobs5').value) + parseInt(document.getElementById('numberOfJobs6').value)
        }
       
  },
  changeToNextContent(now){
      
     
        this.state = now + 1
      
      if (this.state == 0)
      {
        document.getElementById('setBudgetSectionA').hidden = true
        this.displaysectionB = true
       
      }
      else {

        this.state = -1

        this.changeToNextContent(this.state)

      }

        
    
     
    return this.state
  },
  changeToPreviousContent(now){
    this.state2 = now + 1
    if (this.state2 == 0)
      {
        document.getElementById('setBudgetSectionA').hidden = false
        this.displaysectionB = false
        
      }
      
      else {
        this.state = -1
        this.changeToPreviousContent(this.state)
      }

     
     
      
      
      return this.state2
  }

}
 
}
</script>

<style>

.card {

background-color: gold;
box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
transition: 0.3s;
width: 30rem;
height: 10rem;

float:right;
}


.card:hover {
box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}


.container {
padding: 2px 16px;
}

#setBudgetSectionA{
  background-color: gold;
  padding: 2rem;
  width:30vw;
  height:70vh;
  position: relative;
  left:10rem;
}
#setBudgetSectionC{
  background-color: gold;
  padding: 2rem;
  width:90vw;
  height:30rem;
  position:relative;
  left:2rem;
}
#displayBudgetSectionB{
  background-color: #C8A2C8;
  padding: 2rem;
  width:30vw;
  height:70vh;
  position: relative;
  bottom:36rem;
  left:60rem;
}
#displayBudgetSectionC{
  background-color: #C8A2C8;
  padding: 2rem;
  width:30vw;
  height:70vh;
  position:relative;
  top:6rem;
  left:7rem;
}
#displayBudgetSectionA{
  background-color: #C8A2C8;
  padding: 2rem;
  width:30vw;
  height:70vh;
  position: relative;
  bottom:36rem;
  left:50rem;
}
.numberOfJobs{
  border-radius: 0.5rem;
width: 20rem;
height:2rem;
margin:1rem;
}
table, th, td {
border:1px solid black;
}
.BudgetTable{
width:77rem;
height:10rem;
}


th, td{
background-color: #C8A2C8;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
