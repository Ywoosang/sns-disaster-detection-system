<template>
  <div class="item" >
    <p>실시간 SNS</p>
    <div class="sns-wrapper">
      <div class="sns" v-for="(data, index) in getSnsData" :key="index">
        <div class="sns-title">
          <div class="sns-service" v-if="data.service=='instagram'" style="color: rgba(248,45,89,0.9);">
            <font-awesome-icon icon="fa-brands fa-instagram"/> Instagram
          </div>
          <div class="sns-service" v-if="data.service=='twitter'" style="color: rgba(28,156,234,0.9);">
            <font-awesome-icon icon="fa-brands fa-twitter"/> Twitter
          </div>
          <div class="sns-service" v-if="data.service=='naver'" style="color: rgba(0,193,58,0.9);">
            <div style="display: flex; align-items: center;">
                  <img style="width: 15px; margin-right: 6px;" src="../../public/img/naver-icon.png"/>
                  <span style="color: rgb(0,193,58); font-size: 1em; "> Naver Blog</span>    
              </div>
          </div>
          <div class="sns-keyword">
            재난 키워드: {{ data.keyword }}
          </div>
        </div>
        <div class="sns-content">{{ data.sns }}</div>
        <div class="sns-additional">
          <div class="sns-date">{{ data.date }}</div>
          <a v-if="data.service=='twitter'" :href="'http://'+data.link" target="_blank"><font-awesome-icon icon="fa-solid fa-up-right-from-square" /></a>
          <a v-else :href="data.link" target="_blank"><font-awesome-icon icon="fa-solid fa-up-right-from-square" /></a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'SnsMessage',
  computed: {
    ...mapGetters(["getSnsData"])
  }
}
</script>

<style>
.sns-wrapper {
  display: flex;
  flex-direction: column;
  width: 95%;
  height: 95%;
  /* max-height: 80vh; */
  overflow: auto;
  margin-top: 10px;
  padding-right: 6px;
  overflow-y: scroll;
}
.sns-wrapper::-webkit-scrollbar {
  width: 6px;
}
.sns-wrapper::-webkit-scrollbar-thumb {
  /* background-color: #1f2936; */
  /* background-color: rgb(255, 238, 0); */
  background-color: #1ebdbd;
  border-radius: 3px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.sns-wrapper::-webkit-scrollbar-track {
  /* background-color: rgba(240, 235, 235, 0.247); */
  background-color: #1f2936;
  border-radius: 3px;
  box-shadow: inset 0px 0px 3px white;
}

.sns {
  margin-bottom: 20px;
  border: 1px solid rgba(211, 211, 211, 0.466);
  background-color: rgba(211, 211, 211, 0.055);
  padding: 7px 9px;
}
.sns .sns-service {
  font-size: 0.9em;
  min-width: 95px;
}
.sns .sns-content {
  margin: 12px 3px;
  overflow: hidden;
  word-wrap: break-word;
}
.sns .sns-additional {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.sns .sns-additional .sns-date {
  font-size: 0.8em;
}
.sns .sns-additional a{
    color: inherit;
    text-decoration: none; 
    outline: none;
}
.sns-title {
  display: flex;
  justify-content: space-between;
  margin-top:2px;
}
.sns-keyword {
  font-size:0.9em;
  margin-right: 12px;
}
</style>