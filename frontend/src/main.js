import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import router from './router';
import { store } from "./store";
// font-awesome
import { library } from '@fortawesome/fontawesome-svg-core';
import { faHouse } from '@fortawesome/free-solid-svg-icons';
import { faChartLine } from '@fortawesome/free-solid-svg-icons';
import { faComments } from '@fortawesome/free-solid-svg-icons';
import { faTriangleExclamation } from '@fortawesome/free-solid-svg-icons';
import { faTowerBroadcast } from '@fortawesome/free-solid-svg-icons';
import { faVideo } from '@fortawesome/free-solid-svg-icons';
import { faGear } from '@fortawesome/free-solid-svg-icons';
import { faArrowRotateRight } from '@fortawesome/free-solid-svg-icons';
import { faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import { faCircleExclamation } from '@fortawesome/free-solid-svg-icons';
import { faUpRightFromSquare } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

Vue.use(VueRouter);

// font-awesome
library.add(faHouse);
library.add(faChartLine);
library.add(faComments);
library.add(faTriangleExclamation);
library.add(faTowerBroadcast);
library.add(faVideo);
library.add(faGear);
library.add(faArrowRotateRight);
library.add(faInstagram);
library.add(faTwitter);
library.add(faCircleExclamation);
library.add(faUpRightFromSquare);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router: router,
  store: store,
  render: h => h(App),
}).$mount('#app')