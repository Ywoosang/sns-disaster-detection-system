<template>
  <div class="charts-container">
    <div class="item">
      <span>폭설</span>
      <div class="chartLine-wrapper">
        <heavy-snow class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>코로나</span>
      <div class="chartLine-wrapper">
        <corona class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>교통사고</span>
      <div class="chartLine-wrapper">
        <traffic-accident class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>산불</span>
      <div class="chartLine-wrapper">
        <forest-fires class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>붕괴</span>
      <div class="chartLine-wrapper">
        <collaspe class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>폭발</span>
      <div class="chartLine-wrapper">
        <explosion class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>화재</span>
      <div class="chartLine-wrapper">
        <fire class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>태풍</span>
      <div class="chartLine-wrapper">
        <typhoon class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>홍수</span>
      <div class="chartLine-wrapper">
        <flood class="chartLine" />
      </div>
    </div>
    <div class="item">
      <span>전체</span>
      <div class="chart-wrapper">
        <div class="chartLine-wrapper">
          <chart-line class="chartLine" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChartLine from "../components/charts/Line.vue";
import HeavySnow from "../components/charts/HeavySnow.vue";
import Corona from "../components/charts/Corona.vue";
import TrafficAccident from "../components/charts/TrafficAccident.vue";
import ForestFires from "../components/charts/ForestFires.vue";
import Collaspe from "../components/charts/Collaspe.vue";
import Explosion from "../components/charts/Explosion.vue";
import Fire from "../components/charts/Fire.vue";
import Typhoon from "../components/charts/Typhoon.vue";
import Flood from "../components/charts/Flood.vue";

export default {
  name: "Charts",
  components: {
    ChartLine,
    HeavySnow,
    Corona,
    TrafficAccident,
    ForestFires,
    Collaspe,
    Explosion,
    Fire,
    Typhoon,
    Flood,
  },
  data() {
    return {};
  },
};
</script>

<style>
.charts-container {
  font-size: 0.9em;
  height: 100%;
  min-height: 100vh;
  width: 100%;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  padding: 20px 25px;
  grid-gap: 20px;
}

.charts-container .item {
  background-color: #1f2936;
  padding: 15px 20px;
  box-shadow: 1px 1px 10px 2px #a5def023;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  max-height: 30vh;
}

.charts-container .item:nth-child(10) {
  grid-column-start: 2;
  grid-column-end: 5;
  grid-row-start: 3;
  grid-row-end: 4;
}

.charts-container .item .chartLine-wrapper {
  width: 100%;
  height: 100%;
  margin: 15px 0 0 0;
}
</style>
