<template>
  <h1>Monthly/Weekly Overview</h1>
  <section>


    <canvas id="myPieChart2" v-show="showgraph"></canvas>
    <canvas id="myPieChart3" v-show="showgraph"></canvas>
</section>

  <div>
  <canvas id="myChart" v-show="showgraph"></canvas>

</div>
{{ graph }}
      </template>
      
      <script>
      import Chart from 'chart.js/auto'
      
      export default {
        name: 'DashBoardPage',
     
  
       
      data() {
        return {
          array: [],
          onbudget:0,
          offbudget:0,
          income: '0.00',
          expense: '0.00', 
          budget: '0.00',
        moneysaved: '0.00',
        totalexpenditure: '0.00',
        totlaIncome: '0.00',
        
        displayData: ' ',
        options: null,
        showgraph: ' ',
        datas: null,
        graph:  fetch('http://127.0.0.1:5000/visual-overview', { method: "GET", headers:{'Content-Type': 'application/json'}})
  .then(response => {
   return response.text()
  })
  .then(dataz => {
     console.log(dataz)
     
     let res = JSON.parse(dataz)

  
  
     this.showgraph = true
       this.income = String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")
       //olddata =  this.datas["datasets"][0]["data"][0]
       
       
       
       
       console.log(this.income)
       let config = {
        type:'bar',
        data: {
     
     labels: ['January', 'February', 'March', 'April', 'May'],
     datasets: [{
     

   label: 'Income',
   data:[parseInt(this.income[1]), parseInt(this.income[2]), parseInt(this.income[3]), parseInt(this.income[4]),parseInt(this.income[5])] ,
   borderColor: '#000000',
   backgroundColor: '#00000'
 },
 {
   label: 'Expenditure',
   
      
   
      
      data:[
        String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[1]
   ,String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[2], 
   String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[3],
   String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[4],
   String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[5] ],
   borderColor: '#FFF000',
   backgroundColor: '#FFF000',
  

  hoverOffset: 4
  

  }]
 
    
       },
        options:{
          responsive: true,
          aspectRatio : 3,
          scales:{
            y:{
              beginAtZero: true
            }
          }
        }};
       let ctx = document.getElementById('myChart');
       let myChart =  new Chart(ctx, config)
       

       let config3 = {
        type: 'doughnut',
      data: {
    labels:['stock%', 'bonds%', 'cash%'],
  datasets: [{
    label: 'Investment Management',
    data: [res["stock"],res["bonds"], res["cash"]],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4,
        
  }]
    
    }
    ,options:{
          responsive: true,
        aspectRatio: 5,
        plugins:{
               title:{
                display: true,
                text: 'Investment Management Return'
              }},
        layout: {
            padding: {
                left: 0,
                right: 0,
                top: 0,
                bottom: 0,
            }
        }
      }
}
       
       
     

          
        
  

      

        
   
       
       let pie2  =  document.getElementById('myPieChart2')
       let myPieChart2 = new Chart(pie2, config3)
       console.log(this.incomeJan)
       let config4= {
        type:'doughnut',
        data:
   
  {
    labels:['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [{
    label:'money saved',
    data: [parseInt(String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[1]),
    parseInt(String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[2]), 
    parseInt(String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[3]),
    parseInt(String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[4]),
    parseInt(String(res["totalincome"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")[5]),
]
   
    ,

    hoverOffset: 4
    

  }]
},
        options:{
          responsive: true,
         aspectRatio:5,
        plugins:{
               title:{
                display: true,
                text: 'Money saved per month'
              }},
        layout: {
            padding: {
                left: 0,
                right: 0,
                top: 0,
                bottom: 0,
            }
        }

       }
      }

        let pie3 =  document.getElementById('myPieChart3')
       let myPieChart3 = new Chart(pie3, config4)
    
      this.moneysaved =  String(res["moneysaved"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '').split(" ")
      this.totalexpenditure = String(res["cost"]).replace('[', '').replace(']', '').replaceAll(',', '').replaceAll("'", '')

      
      myChart;
      myPieChart2;
      myPieChart3;
  })
  }

        
  
      
    }
      }
    
      </script>
      
      <style scoped>
      #container{
          background-color: gold;
          box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 30rem;
  height: 10rem;
          position: relative;
          top:18rem;
       
       
      }
      #card{
        margin:2rem;
        background-color: gold;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 30rem;
  height: 10rem;
      }
      #myChart{
     
        position: relative;
        left: 40rem;
        bottom:48rem;
        width:400vw;
        height:400vh;
      }
     
      #myPieChart2{
      
        margin:4rem;
        position:relative;
        bottom:5rem;
        right:40rem;
 }
  #myPieChart3{
  
   position:relative;
   top:5rem;
   right:40rem;
 }
      </style>
      