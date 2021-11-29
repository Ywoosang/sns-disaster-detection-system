<template>
    <div class="sns-container">
        <!-- 인스타그램 -->
        <div class="sns-item" id="mobile-hide">
            <span style="color: rgb(248,45,89); font-size: 1em;"><font-awesome-icon icon="fa-brands fa-instagram"/> Instagram</span>
            <div class="sns-wrapper">
                <div class="sns" v-for="(data, index) in getInstagramData" :key="index">
                    <div class="sns-title">
                        <div class="sns-keyword">재난 키워드: {{ data.keyword }}</div>
                    </div>
                    <div class="sns-content">{{ data.sns }}</div>
                    <div class="sns-additional">
                        <div class="sns-date">{{ data.date }}</div>
                        <a :href="data.link" target="_blank"><font-awesome-icon icon="fa-solid fa-up-right-from-square" /></a>  
                    </div>
                    
                </div>
            </div>
        </div>
        <!-- 트위터 -->
        <div class="sns-item" id="mobile-hide">
            <span style="color: rgb(28,156,234); font-size: 1em;"><font-awesome-icon icon="fa-brands fa-twitter"/> Twitter</span>
            <div class="sns-wrapper">
                <div class="sns" v-for="(data, index) in getTwitterData" :key="index">
                    <div class="sns-title">
                        <div class="sns-keyword">재난 키워드: {{ data.keyword }}</div>
                    </div>
                    <div class="sns-content">{{ data.sns }}</div>
                    <div class="sns-additional">
                        <div class="sns-date">{{ data.date }}</div>
                        <a :href="'http://'+data.link" target="_blank"><font-awesome-icon icon="fa-solid fa-up-right-from-square" /></a>      
                    </div>
                </div>
            </div>
        </div>
        <!-- 네이버 블로그 -->
        <div class="sns-item" id="mobile-hide">
            <div style="display: flex; align-items: center;">
                <img style="width: 15px; margin-right: 6px;" src="../../public/img/naver-icon.png"/>
                <span style="color: rgb(0,193,58); font-size: 1em; "> Naver Blog</span>    
            </div>
            
            <div class="sns-wrapper">
                <div class="sns" v-for="(data, index) in getNaverData" :key="index">
                    <div class="sns-title">
                        <div class="sns-keyword">재난 키워드: {{ data.keyword }}</div>
                    </div>
                    <div class="sns-content">{{ data.sns }}</div>
                    <div class="sns-additional">
                        <div class="sns-date">{{ data.date }}</div>
                        <a :href="data.link" target="_blank"><font-awesome-icon icon="fa-solid fa-up-right-from-square" /></a>                       
                    </div>
                </div>
            </div>
        </div>
        <!-- 전체 -->
        <div class="sns-item" id="mobile-view">
            <sns-message/>
        </div>
    </div>
</template>

<script>
import SnsMessage from '../components/SnsMessage.vue'
import { mapGetters } from 'vuex';

export default {
    name: 'Sns',
    components: {
        SnsMessage
    },
    computed: {
        ...mapGetters(["getInstagramData", "getTwitterData", "getNaverData"])
    }
}
</script>

<style>
.sns-container {
  font-size: 0.9em;
  width: 100%;
  padding: 20px 25px;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 20px;
  overflow-y: hidden;
}

.sns-container .sns-item {
  background-color: #1f2936;
  padding: 15px 20px;
  box-shadow: 1px 1px 10px 2px #a5def023;
  display: flex;
  overflow:hidden;
  flex-direction: column;
  box-sizing: border-box;
}

.sns-container .sns-item .sns-wrapper {
  flex:1;
  display: flex;
  flex-direction: column;
  overflow-y:scroll;
  width: 95%;
  padding-right: 6px;
  margin-top: 20px;
}

.sns-container .sns-item .sns-wrapper::-webkit-scrollbar {
  width: 6px;
}
.sns-container .sns-item .sns-wrapper::-webkit-scrollbar-thumb {
  background-color: #1ebdbd;
  border-radius: 3px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.sns-container .sns-item .sns-wrapper::-webkit-scrollbar-track {
  background-color: #1f2936;
  border-radius: 3px;
  box-shadow: inset 0px 0px 3px white;
}


.sns-container .sns-item .sns-wrapper .sns {
  margin-bottom: 20px;
  border: 1px solid rgba(211, 211, 211, 0.466);
  background-color: rgba(211, 211, 211, 0.055);
  padding: 7px 15px;
}
.sns-container .sns-item .sns-wrapper .sns .sns-content {
  overflow: hidden;
  word-wrap: break-word;
}
.sns-container .sns-item .sns-wrapper .sns .sns-date {
  font-size: 0.8em;
}
.sns-container .sns-item .sns-wrapper .sns .sns-additional {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.sns-additional a{
    color: inherit;
    text-decoration: none; 
    outline: none;
}
.sns-keyword {
    width:100%;
    text-align: right;
}
.sns-container #mobile-view {
    display: none;
}

@media (max-width: 767px) {
    .sns-container #mobile-view {
        display: block;
    }
    .sns-container {
        width: 100%;
        padding: 20px 25px;
        display: flex;
    }
    .sns-container .sns-item {
        overflow: hidden;
    }
}
</style>