<template>
    <div class="ping-container">
        <button @click="ping">Ping Test</button>
        <div class="ping-content">
            <div class="ping-item">
                <hr>
                nlp
                <hr>
                <div v-for="(data,index) in nlp" :key="index + '1'">
                    {{ data }}
                </div>
            </div>
            <div class="ping-item">
                <hr>
                트위터
                <hr>
                <div v-for="(data,index) in twitter" :key="index + '1'">
                    {{ data }}
                </div>
            </div>
            <div class="ping-item">
                <hr>
                네이버
                <hr>
                <div v-for="(data,index) in naver" :key="index + '1'">
                    {{ data }}
                </div>
            </div>
               <div class="ping-item">
                <hr>
                인스타그램
                <hr>
                <div v-for="(data,index) in instagram" :key="index + '1'">
                    {{ data }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return {
            instagram: [],
            message : '',
            twitter : [],
            naver: [],
            nlp: []
        }
    },
    methods : {
        async ping(){
            const instagram= await axios.get('https://disasterback.cf/api/instagram/ping');
            this.instagram = instagram.data.data
            const twitter = await axios.get('https://disasterback.cf/api/twitter/ping');
            this.twitter = twitter.data.data
            const naver = await axios.get('https://disasterback.cf/api/naver/ping');
            this.naver = naver.data.data
            const nlp = await axios.get('https://disasterback.cf/api/model/ping');
            this.nlp = nlp.data.data
        }
    }
    
}
</script>

<style scoped>
*{
    overflow:auto;
}
.ping-container {
    width: 100%;
}
</style>