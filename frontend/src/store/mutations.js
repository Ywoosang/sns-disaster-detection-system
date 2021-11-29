export default {
    showModal(state) {
        return state.isViewModal = true;
    },
    closeModal(state) {
        return state.isViewModal = false;
    },
    showFinishModal(state) {
        return state.isSendMail = true;
    },
    closeFinishModal(state) {
        return state.isSendMail = false;
    },
    updateData(state,payload) {
        const newCrawlingData = payload.newCrawlingData;
        const date = payload.date;
        // crawlingData 업데이트
        state.crawlingData = newCrawlingData;
        // 키워드별 언급량 계산
        const counts = Array(9).fill(0);
        state.crawlingData.forEach((data)=>{
            for(let index=0; index<9; index++) {
                if(data.keyword == state.keywords[index]) {
                    counts[index]++;
                    break;
                }
            }
        });
        // barData 업데이트
        const newBarData = counts;
        state.barData.datasets.forEach((dataset) => {
            dataset.data = newBarData;
        })
        // rankData, lineData 업데이트 준비
        const newRankData = [];
        const newLineData = [];
        const [hours, minutes] = [date.split('-')[3],date.split('-')[4]];
        const x = `${hours}:${minutes}`;
        counts.forEach((y, index)=>{
            newRankData.push({
                label: state.keywords[index],
                y
            });
            newLineData.push({
                x,
                y
            });
        })
        // rankData 업데이트
        newRankData.sort(function(a, b) {
            if(a.y < b.y) return 1;
            if(a.y > b.y) return -1;
            if(a.y === b.y) return 0;
        });
        state.rankData = newRankData.map(data => data.label);
        // lineData 업데이트 
        if(state.lineData.datasets[0].data.length > 10) {
            state.lineData.labels.shift();
            state.lineData.labels.push(x);
            state.lineData.datasets.forEach((dataset, index) => {
                dataset.data.shift();
                dataset.data.push(newLineData[index]);
            })
        } else {
            state.lineData.labels.push(x);
            state.lineData.datasets.forEach((dataset, index) => {
              dataset.data.push(newLineData[index]);
            })
        }
    },
    addSnsData(state, data) {
        if (data.service == 'instagram') {
            if(state.snsInstagram.length > 100) {
                state.snsInstagram.pop();
            }
            state.snsInstagram.unshift(data);
        }
        else if(data.service == 'twitter') {
            if(state.snsTwitter.length > 100) {
                state.snsTwitter.pop();
            }
            state.snsTwitter.unshift(data);
        }
        else {
            if(state.snsNaver.length > 100) {
                state.snsNaver.pop();
            }
            state.snsNaver.unshift(data);
        }
    },
    updateSnsData(state) {
        state.snsData = [...state.snsInstagram,...state.snsTwitter,...state.snsNaver];
        state.snsData.sort(function (a, b) {
            if (a.date < b.date) return 1;
            if (a.date > b.date) return -1;
            if (a.date === b.date) return 0;
        }); 
    }
}