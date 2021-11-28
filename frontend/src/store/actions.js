import toDateFormat from "../utils/dateFormat";
import axios from 'axios';
export default {
    async setData(context){
        const baseDate = new Date();
        // baseDate 가 20 분 전 설정
        baseDate.setMinutes(baseDate.getMinutes() -200);
        for(let i=0; i <= 9; i ++){
            //20 분 전
            const start = toDateFormat(baseDate);
            baseDate.setMinutes(baseDate.getMinutes() + 20);
            const end = toDateFormat(baseDate);
            console.log('setCrawlingDataSet',start,end);
            const origin = 'http://localhost:8080';
            const query = `?start=${start}&end=${end}`;
            const urls = [
                origin+'/api/instagram/data'+query,
                origin+'/api/twitter/data'+query,
                origin+'/api/naver/data'+query
            ]
            const promises = [];
            for(const url of urls){
                promises.push(axios.get(url))
            }
            const responses = await Promise.all(promises);
            const newCrawlingData = [];
            for(const response of responses){
                const dataset = response.data.data;
                for(const data of dataset){
                    newCrawlingData.push(data);
                }
            }
            console.log(newCrawlingData)
            const payload = {
                newCrawlingData,
                    date: end
            }
            context.commit('updateData',payload);
        }
    },
    async setSnsData(context){
        const startDate = new Date();
        const endDate = new Date()
        startDate.setMinutes(startDate.getMinutes() - 60*12)
        const start = toDateFormat(startDate);
        const end = toDateFormat(endDate);
        console.log('setSnsData',start,end);
        const origin = 'http://localhost:8080';
        const query = `?start=${start}&end=${end}`;
        const url = origin+'/api/model/data'+query;
        console.log('모델 요청 주소',url)
        const response = await axios.get(url);
        const newModelData = response.data.data;
        // const getTime = 2*60*1000;
        newModelData.sort(function(a, b) {
            if(a.y < b.y) return -1;
            if(a.y > b.y) return 1;
            if(a.y === b.y) return 0;
        });
        const maxLen = 50;
        const newLen = newModelData.length; 
        let startIndex = 0;
        if(newLen > maxLen) {
            startIndex = newLen - maxLen; 
        }
        // const loadTime = getTime / newLen;
        for(let i=startIndex; i<newLen; i++) {
            // await new Promise(resolve => setTimeout(resolve, loadTime));
            const data = newModelData[i];
            console.log('모델 데이터',data)
            context.commit('addSnsData', data);
        }
    },
    async getNewServerData(context) {
        try{
            const startDate = new Date();
            const endDate = new Date();
            startDate.setMinutes(startDate.getMinutes() -20)
            const start = toDateFormat(startDate);
            const end = toDateFormat(endDate);
            console.log('getNewServerData',start, end);
            const origin = 'http://localhost:8080';
            const query = `?start=${start}&end=${end}`;
            const urls = [
                origin+'/api/instagram/data'+query,
                origin+'/api/twitter/data'+query,
                origin+'/api/naver/data'+query
            ]
            const promises = []
            for(const url of urls){
                promises.push(axios.get(url))
            }
            const responses = await Promise.all(promises);
            const newCrawlingData = [];
            for(const response of responses){
                const dataset = response.data.data;
                for(const data of dataset){
                    newCrawlingData.push(data);
                }
            }
            const payload =  {
                newCrawlingData, 
                date : end
            }
            context.commit('updateData',payload);
        }catch(error) {
            console.log(error)
        }
    },
    async getNewModelData(context) {
        try{
            const getTime = 2*60*1000;
            // 10분마다 모델 데이터 요청
            const startDate = new Date();
            const endDate = new Date();
            startDate.setMinutes(startDate.getMinutes() - 60*12);
            const start = toDateFormat(startDate);
            const end = toDateFormat(endDate);
            console.log('getNewModelData',start,end);
            const origin = 'http://localhost:8080';
            const query = `?start=${start}&end=${end}`;
            const url = origin+'/api/model/data'+query;
            const response = await axios.get(url);
            const dataset = response.data.data;
            const newModelData = dataset;
            newModelData.sort(function(a, b) {
                if(a.y < b.y) return -1;
                if(a.y > b.y) return 1;
                if(a.y === b.y) return 0;
            });
            // snsData의 최대 길이에 맞춰 이전 데이터 삭제
            context.commit('deleteSnsData',newModelData);
            // 일정 시간 간격으로 snsData 업데이트
            const newLen = newModelData.length; 
            // const loadTime = getTime / newLen;
            const loadTime = 0;
            for(let i=0; i<newLen; i++) {
                await new Promise(resolve => setTimeout(resolve, loadTime));
                const data = newModelData[i];
                context.commit('addSnsData', data);
            }
            await new Promise(resolve => setTimeout(resolve, getTime));
        } catch(error){
            console.log(error)
        }
    }
}