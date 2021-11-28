<template>
  <div class="item">
    <p>실시간 재난 언급량 </p>
    <div class="chart-wrapper">
      <div class="chartRank">
        <div class="rank-item" v-for="(keyword, index) in getRankData" :key="index">
          <div class="rank">{{ index + 1 }}</div>
          <div class="name">{{ keyword }}</div>
        </div>
      </div>
      <div class="chartBar-wrapper">
        <chart-bar class="chartBar" />
      </div>
    </div>
  </div>
</template>

<script>
import ChartBar from "./charts/Bar.vue";
import { mapGetters } from "vuex";

export default {
  name: "Rank",
  components: {
    ChartBar,
  },
  computed: {
    ...mapGetters(["getRankData"]),
  },
};
</script>

<style>
.chartBar-wrapper {
  margin: 5px 5px 5px 5px;
  height: 100%;
  box-sizing: border-box;
}
.chartBar-wrapper{
  width: 100%;
  height: 100%;
}

.chartRank {
  margin: 5px 5px;
  min-width: 150px;
  width: 200px;
  max-width: 250px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.chartRank .rank-item {
  width: 70%;
  display: flex;
}
.chartRank .rank-item .rank {
  color: #17a9a8;
  margin-right: 20px;
}
.chartRank .rank-item .name {
  width: 60px;
}
</style>
