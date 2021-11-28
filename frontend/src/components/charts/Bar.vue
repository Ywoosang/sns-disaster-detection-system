<template>
  <canvas ref="chartBar"></canvas>
</template>
<script>
import Chart from "chart.js";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      chartBar: null,
      options: {
        maintainAspectRatio: false,
        responsive: true,
        hoverBackgroundColor: [
          "rgba(209, 216, 224,0.5)", // 흰
          "rgba(252, 92, 101,0.5)", // 빨
          "rgba(69, 170, 242,0.5)", // 파
          "rgba(253, 150, 68,0.5)", // 주
          "rgba(254, 211, 48,0.5)", //노
          "rgba(38, 222, 129,0.5)", //초
          "rgba(165, 94, 234,0.5)", //보
          "rgba(119, 140, 163,0.5)", //회
          "rgba(75, 123, 236,0.5)", //남
        ],
        legend: {
          display: false,
        },
        tooltips: {
          backgroundColor: "rgb(23,30,39)",
          bodyFontColor: "rgba(255, 255, 255, 0.68)",
          titleFontColor: "rgba(255, 255, 255, 0.88)",
        },
      },
    };
  },
  computed: {
    ...mapGetters(["getBarData", "getBarDataData"])
  },
  async mounted() {
    await this.drawChart();
  },
  methods: {
    drawChart() {
      const ctx = this.$refs.chartBar.getContext("2d");
      const chartBar = new Chart(ctx, {
        type: "bar",
        data: this.getBarData,
        options: this.options,
      });
      this.chartBar = chartBar;
    },
  },
  watch: {
    getBarDataData() {
      this.chartBar.update();
    }
  }
};
</script>
