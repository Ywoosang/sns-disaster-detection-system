<template>
  <main>
    <nav-bar/> 
    <modal v-if="getIsViewModal" />
    <finish-modal v-if="getIsSendMail"/>
    <router-view/>
  </main>
</template>

<script>
import NavBar from './components/common/Nav.vue'
import Modal from './components/common/Modal.vue'
import FinishModal from './components/common/FinishModal.vue';
import { mapActions, mapGetters } from "vuex";

export default {
  name: 'App',
  components: {
    NavBar,
    Modal,
    FinishModal,
  },
  computed: {
    ...mapGetters(["getIsViewModal", "getIsSendMail", "getCrawlingData", "getModelData"]),
  },
  methods: {
    ...mapActions(["getNewServerData", "getNewModelData","setSnsData","setData"])
  },
  async created() {
    // const baseDate = new Date();
    // const start = toDateFormat(baseDate.setMinutes(baseDate.getMinutes() -20));
    // const end = toDateFormat(baseDate);
    // const payload = {
    //   start,
    //   end
    // }
    // console.log(start,end);
    // this.getServerData(payload);
    // this.getModelData(payload);
    this.setSnsData();
    this.setData();
    // await new Promise(resolve=>{
    //   setTimeout(() => {
    //     resolve()
    //   },1000)

    // })
    setInterval(()=> {
        this.getNewServerData()
    },10*60*1000)


  },
  watch : {
    // getCrawlingData() {
    //   this.getNewServerData();
    // },
    // getModelData() {
    //   this.getNewModelData();
    // }
  }
}
</script>

<style>
* {
  /* border: 1px solid red; */
}

html {
  height:100%;
}

body {
  margin: 0;
  height:100%;
  background-color: #161d26;
  /* color: white; */
  color: rgba(255, 255, 255, 0.788);
}

main {
  overflow-y: hidden;
  height:100%;
  overflow-x:hidden;
  display: flex;
}
</style>
