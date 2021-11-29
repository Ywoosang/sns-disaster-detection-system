import toDateFormat from "../utils/dateFormat";
import axios from 'axios';
export default {
    async setData(context) {
        const baseDate = new Date();
        // baseDate 가 20 분 전 설정
        baseDate.setMinutes(baseDate.getMinutes() - 200);
        for (let i = 0; i <= 9; i++) {
            //20 분 전
            const start = toDateFormat(baseDate);
            baseDate.setMinutes(baseDate.getMinutes() + 20);
            const end = toDateFormat(baseDate);
            const origin = 'https://disasterback.cf';
            const query = `?start=${start}&end=${end}`;
            const urls = [
                origin + '/api/instagram/data' +  `?start=2021-11-11-11-11&end=${end}`,
                origin + '/api/twitter/data' + query,
                origin + '/api/naver/data' + query
            ]
            const promises = [];
            for (const url of urls) {
                promises.push(axios.get(url))
            }
            const responses = await Promise.all(promises);
            const newCrawlingData = [];
            for (const response of responses) {
                const dataset = response.data.data;
                for (const data of dataset) {
                    newCrawlingData.push(data);
                }
            }
            const payload = {
                newCrawlingData,
                date: end
            }
            context.commit('updateData', payload);
        }
    },
    async setSnsData(context) {
        const startDate = new Date();
        const endDate = new Date()
        startDate.setMinutes(startDate.getMinutes() - 100000)
        const start = toDateFormat(startDate);
        const end = toDateFormat(endDate);
        const origin = 'https://disasterback.cf';
        const query = `?start=${start}&end=${end}`;
        const url = origin + '/api/model/data' + query;
        const response = await axios.get(url);
        const newModelData = response.data.data;
        // const getTime = 2*60*1000;
        newModelData.sort(function (a, b) {
            if (a.date < b.date) return -1;
            if (a.date > b.date) return 1;
            if (a.date === b.date) return 0;
        }); 
        const newLen = newModelData.length;
        // const loadTime = getTime / newLen;
        for (let i = 0; i < newLen; i++) {
            // await new Promise(resolve => setTimeout(resolve, loadTime));
            const data = newModelData[i];
            context.commit('addSnsData', data);
        }
        context.commit('updateSnsData');
    },
    async getNewServerData(context) {
        try {
            const startDate = new Date();
            const endDate = new Date();
            startDate.setMinutes(startDate.getMinutes() - 20)
            const start = toDateFormat(startDate);
            const end = toDateFormat(endDate);
            const origin = 'https://disasterback.cf';
            const query = `?start=${start}&end=${end}`;
            const urls = [
                origin + '/api/instagram/data' + query,
                origin + '/api/twitter/data' + query,
                origin + '/api/naver/data' + query
            ]
            const promises = []
            for (const url of urls) {
                promises.push(axios.get(url))
            }
            const responses = await Promise.all(promises);
            const newCrawlingData = [];
            for (const response of responses) {
                const dataset = response.data.data;
                for (const data of dataset) {
                    newCrawlingData.push(data);
                }
            }
            const payload = {
                newCrawlingData,
                date: end
            }
            context.commit('updateData', payload);
        } catch (error) {
            console.log(error)
        }
    },
    async getNewModelData(context) {
        try {
            const getTime = 2 * 60 * 1000;
            // 10분마다 모델 데이터 요청
            const startDate = new Date();
            const endDate = new Date();
            startDate.setMinutes(startDate.getMinutes() - 60 * 12);
            const start = toDateFormat(startDate);
            const end = toDateFormat(endDate);
            const origin = 'https://disasterback.cf';
            const query = `?start=${start}&end=${end}`;
            const url = origin + '/api/model/data' + query;
            const response = await axios.get(url);
            const dataset = response.data.data;
            const newModelData = dataset;
            newModelData.sort(function (a, b) {
                if (a.date < b.date) return -1;
                if (a.date > b.date) return 1;
                if (a.date === b.date) return 0;
            });
            // snsData 업데이트
            const newLen = newModelData.length;
            // const loadTime = getTime / newLen;
            const loadTime = 0;
            for (let i = 0; i < newLen; i++) {
                await new Promise(resolve => setTimeout(resolve, loadTime));
                const data = newModelData[i];
                context.commit('addSnsData', data);
            }
            context.commit('updateSnsData');
            await new Promise(resolve => setTimeout(resolve, getTime));
        } catch (error) {
            console.log(error)
        }
    }
}