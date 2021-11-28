<template>
    <div>
        <button @click="ping">Ping Test</button>
          <hr>
        nlp
        <hr>
        <div v-for="(data,index) in nlp" :key ="index + '0'">
            {{ data }}
        </div>
        <hr>
        인스타
        <hr>
        <div v-for="(data,index) in instagram" :key="index + '1'">
            {{ data }}
        </div>
        <hr>
        트위터
        <hr>
        <div v-for="(data,index) in twitter" :key ="index + '2'">
            {{ data }}
        </div>
        <hr>
        네이버
        <hr>
        <div v-for="(data,index) in naver" :key ="index + '3'">
            {{ data }}
        </div>


    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return {
            instagram: [],
            twitter : [],
            naver: [],
            nlp: []
        }
    },
    methods : {
        async ping(){
            let a = await axios.get('http://localhost:8080/api/instagram/ping');
            this.instagram = a.data.data
            let b = await axios.get('http://localhost:8080/api/twitter/ping');
            this.twitter = b.data.data
            let c = await axios.get('http://localhost:8080/api/naver/ping');
            this.naver = c.data.data
            let d = await axios.get('http://localhost:8080/api/model/ping');
            this.nlp = d.data.data
        }
    }
    
}
</script>

<style scoped>
*{
    overflow:auto;
}

</style>