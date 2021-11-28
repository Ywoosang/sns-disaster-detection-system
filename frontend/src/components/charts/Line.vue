<template>
  <canvas ref="chartLine"></canvas>
</template>

<script>
import Chart from "chart.js";
import { mapGetters } from "vuex";
Chart.defaults.global.defaultFontColor = 'rgba(255, 255, 255, 0.58)';
Chart.defaults.global.elements.line.tension = 0;

export default {
  data() {
    return {
      chartLine: null,
      options: {
        maintainAspectRatio: false,
        responsive: true,
        legend:{
            position: 'right',
            labels: {
                boxWidth: 20,
                padding: 15 
            }
        },
        tooltips: {
            mode: 'nearest',
            position: 'average',
            backgroundColor: 'rgb(23,30,39)',
            bodyFontColor: 'rgba(255, 255, 255, 0.68)',
            titleFontColor: 'rgba(255, 255, 255, 0.88)'
        },
        scales: {
            xAxes: [{
            }]
        },
      },
    };
  },
  computed: {
    ...mapGetters(["getLineData", "getLineDataLabels"])
  },
  async mounted() {
    await this.drawChart();
  },
  methods: {
    drawChart() {
      const ctx = this.$refs.chartLine.getContext("2d");
      const chartLine = new Chart(ctx, {
        type: "line",
        data: this.getLineData,
        options: this.options,
      });
      this.chartLine = chartLine;
    },
  },
  watch: {
    getLineDataLabels() {
      this.chartLine.update();
    }
  }
};
</script>

<style></style>
