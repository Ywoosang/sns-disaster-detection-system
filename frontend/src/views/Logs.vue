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
                <!-- <div v-for="(data,index) in instagram" :key="index + '1'">
                    {{ data }}
                </div> -->
                <div>
                    {{ message}}
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
            // instagram: [],
            message : '',
            twitter : [],
            naver: [],
            nlp: []
        }
    },
    methods : {
        async ping(){
            // let a = await axios.get('http://localhost:8080/api/instagram/ping');
            this.message =  {
                        status : "Stacktrace:#0 0x558687213949 unknown",
                        message : "Instagram blocked the Selenium Browser",
                        issue : "https://github.com/InstaPy/InstaPy/issues/4625"
                    }
            let b = await axios.get('https://disasterback.cf/api/twitter/ping');
            this.twitter = b.data.data
            let c = await axios.get('https://disasterback.cf/api/naver/ping');
            this.naver = c.data.data
            let d = await axios.get('https://disasterback.cf/api/model/ping');
            this.nlp = d.data.data
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