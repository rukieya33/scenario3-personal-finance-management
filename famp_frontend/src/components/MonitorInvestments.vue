<template>

    <h1>Monitor Investment:</h1>
      <h2>Current Investment</h2>

      <h3>{{ InvestmentDetails }}</h3>
      <h3>{{ company }}</h3>
      <h3>{{ companyearnings }}</h3>
      <h3>{{ companyleverage }}</h3>
      <h3>{{ moneyinvested }}</h3>
      <h3>{{ expectedIncome }}</h3>
      <button>Start Monitoring</button>
    
      <router-link to="/manage-investment">Go Back </router-link>
    </template>
    <script>
  
  
   // Current tab is set to be the first tab (0)
  
  
  
  
    export default {
      name: 'MonitorInvestment',
    
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
          nameofCost : "",
          currentTab : 0,
          stock: " ",
          expectedIncome : " ",
          company: "",
          companyearnings: "",
          companyleverage: "",
          moneyinvested : "",
          array: [],
          InvestmentDetails :   fetch('http://127.0.0.1:5000/monitor_investment', { method: "GET", headers:{'Content-Type': 'application/json'},
})
.then(response => {
 return  response.json()
})
.then(data => {

console.log(data)
   this.showstock = true
   
  
   this.company =  data["companyname"]
   this.companyearnings = data["earnings"]
   this.companyleverage = data["leverage"]
   this.moneyinvested = data["savings"]
   this.expectedIncome = data["income"]
  
   this.array.push({"comp" : data["company"], 
  "compearnings" : data["earnings"],
"compleverage" : data["leverage"],
"moneyinvested" : data["moneyinvested"],
"expectedIncome" : data["company"]})
  
})
        }
      },
      methods:{
          validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[this.currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
      // If a field is empty...
      if (y[i].value == "") {
        // add an "invalid" class to the field:
        y[i].className += " invalid";
        // and set the current valid status to false:
        valid = false;
      }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
      document.getElementsByClassName("step")[this.currentTab].className += " finish";
    }
    return valid; // return the valid status
  },
          nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !this.validateForm()) return false;
    // Hide the current tab:
    x[this.currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    this.currentTab = this.currentTab + n;
    // if you have reached the end of the form... :
    if (this.currentTab >= x.length) {
      //...the form gets submitted:
      document.getElementById("regForm").submit();
      return false;
    }
    // Otherwise, display the correct tab:
    this.showTab(this.currentTab);
  },
  showTab(n) {
    // This function will display the specified tab of the form ...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    // ... and fix the Previous/Next buttons:
    if (n == 0) {
      document.getElementById("prevBtn").style.display = "none";
    } else {
      document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
      document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
      document.getElementById("nextBtn").innerHTML = "Next";
    }
    // ... and run a function that displays the correct step indicator:
    this.fixStepIndicator(n)
  },
  fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
      x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class to the current step:
    x[n].className += " active";
  },
       
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
    
    <style>* {
      box-sizing: border-box;
    }
    
    body {
      background-color: #f1f1f1;
    }
    
    #regForm {
      background-color: #ffffff;
      margin: 100px auto;
      font-family: Raleway;
      padding: 40px;
      width: 70%;
      min-width: 300px;
    }
    
    h1 {
      text-align: center;  
    }
    
    input {
      padding: 10px;
      width: 20%;
      font-size: 17px;
      font-family: Raleway;
      border: 1px solid #aaaaaa;
    }
    
    /* Mark input boxes that gets an error on validation: */
    input.invalid {
      background-color: #ffdddd;
    }
    
    /* Hide all steps by default: */
    .tab {
      display: block;
    }
    
    button {
      background-color: #04AA6D;
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      font-size: 17px;
      font-family: Raleway;
      cursor: pointer;
    }
    
    button:hover {
      opacity: 0.8;
    }
    
    #prevBtn {
      background-color: #bbbbbb;
    }
    
    /* Make circles that indicate the steps of the form: */
    .step {
      height: 15px;
      width: 15px;
      margin: 0 2px;
      background-color: #bbbbbb;
      border: none;  
      border-radius: 50%;
      display: inline-block;
      opacity: 0.5;
    }
    
    .step.active {
      opacity: 1;
    }
    
    /* Mark the steps that are finished and valid: */
    .step.finish {
      background-color: #04AA6D;
    }
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
  
    

  

    </style>
    