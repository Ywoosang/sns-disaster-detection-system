<template>
  <canvas ref="chartLine" style="width: 100%; height: 100% !important"></canvas>
</template>

<script>
import Chart from "chart.js";
import { mapGetters } from "vuex";
Chart.defaults.global.defaultFontColor = "rgba(255, 255, 255, 0.58)";
Chart.defaults.global.elements.line.tension = 0;

export default {
  data() {
    return {
      chartLine: null,
    };
  },
  computed: {
    ...mapGetters([
      "getLineDataLabels",
      "getLineDataDatasets",
      "getLineOptions",
    ]),
  },
  async mounted() {
    await this.drawChart();
  },
  methods: {
    drawChart() {
      const ctx = this.$refs.chartLine.getContext("2d");
      const chartLine = new Chart(ctx, {
        type: "line",
        data: {
          labels: this.getLineDataLabels,
          datasets: [this.getLineDataDatasets[8]],
        },
        options: this.getLineOptions
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
