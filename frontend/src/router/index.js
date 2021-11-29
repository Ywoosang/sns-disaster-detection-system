import Home from '../views/Home.vue'
import Charts from '../views/Charts.vue'
import Sns from '../views/Sns.vue'
import VueRouter from 'vue-router'
import Logs from '../views/Logs.vue';
import Demo from '../views/Demo.vue';
import Settings from '../views/Settings.vue';

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
        },
        {
            path: '/demo',
            component: Demo,
            meta: {
                title: "대시보드 > Demo"
              }
        },
        {
            path: '/settings',
            component: Settings,
            meta: {
                title: "대시보드 > Settings"
              }
        }
    ]
})


router.afterEach((to) => {
    if(to.meta.title){
      document.title = to.meta.title;
    }
});

export default router