import { createRouter, createWebHistory } from 'vue-router'

import DashBoardPage from '../views/DashBoardPage.vue'
import HomePage from '../views/Homepage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import ProfilePage from '../views/ProfilePage.vue'
import SetBudget from '../views/SetBudgets.vue'
import ManageInvestment from '../views/ManageInvestment.vue'

import MonitorInvestment from '../components/MonitorInvestments.vue'
import FinancialStatment from '../components/FinancialStatementAnalysis.vue'



const  routes =  [
  { path: '/', component: HomePage , props:true},
  { path: '/monitor-investment', component: MonitorInvestment,  props:true},
  { path: '/financial-statement', component: FinancialStatment,  props:true},
  { path: '/dashboard',  component: DashBoardPage ,props:true  },
  { path: '/register' , component: RegisterPage,props:true  },
  { path: '/myprofile', component: ProfilePage ,props:true },
  { path: '/budgets', component: SetBudget, props:true},
  { path: '/track-spending' , props:true},
  { path: '/manage-investment', component:ManageInvestment, props:true},
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: 'active-tab'
})

  

export default router
