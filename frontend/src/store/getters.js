export default {
    getIsViewModal(state) {
        return state.isViewModal;
    },
    getIsSendMail(state) {
        return state.isSendMail;
    },
    getLineData(state) {
        return state.lineData;
    },
    getLineDataLabels(state){
        return state.lineData.labels;
    },
    getLineDataDatasets(state) {
        return state.lineData.datasets;
    },
    getLineOptions(state) {
        return state.lineOptions;
    },
    getBarData(state) {
        return state.barData;
    },
    getBarDataData(state) {
        return state.barData.datasets[0].data;
    },
    getRankData(state) {
        return state.rankData;
    },
    getKewords(state) {
        return state.keywords;
    },
    getSnsData(state) {
        return state.snsData;
    },
    getInstagramData(state) {
        return state.snsInstagram;
    },
    getTwitterData(state) {
        return state.snsTwitter;
    },
    getNaverData(state) {
        return state.snsNaver;
    }
}