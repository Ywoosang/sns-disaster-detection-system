<template>
  <div class="item">
    <p>시간대별 재난 언급량</p>
    <div class="chart-wrapper">
      <div class="chartLine-wrapper">
        <chart-line class="chartLine"/>
      </div>
    </div>
  </div>
</template>

<script>
import ChartLine from "./charts/Line.vue";

export default {
  name: "TimeSeries",
  components: {
    ChartLine
  }
};
</script>

<style>
.chartLine-wrapper{
  box-sizing: border-box;
  width: 100% !important;
  height: 100% !important;
}
</style>
