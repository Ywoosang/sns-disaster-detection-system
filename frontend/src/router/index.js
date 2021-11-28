import Home from '../views/Home.vue'
import Charts from '../views/Charts.vue'
import Sns from '../views/Sns.vue'
import VueRouter from 'vue-router'
import Logs from '../views/Logs.vue';

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            redirect: "/dashboard"
        },
        {
            path: '/dashboard',
            component: Home,
            meta : {
                title : "SNS 재난 모니터링 시스템"
            }
        },
        {
            path: '/charts',
            component: Charts,
            meta: {
                title: "대시보드 > Charts"
            }
        },
        {
            path: '/sns',
            component: Sns,
            meta: {
                title: "대시보드 > SNS"
            }
        },
        {
            path: '/logs',
            component: Logs,
            meta: {
                title: "대시보드 > Logs"
              }
        }
    ]
})


router.afterEach((to, from) => {
    if(to.meta.title){
      document.title = to.meta.title;
      console.log(from)
    }
});

export default router