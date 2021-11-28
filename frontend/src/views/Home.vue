<template>
  <div class="home-container">
    <rank/>
    <time-series/>
    <sns-message/>   
  </div>
</template>

<script>
import Rank from '../components/Rank.vue'
import TimeSeries from '../components/TimeSeries.vue'
import SnsMessage from '../components/SnsMessage.vue'

export default {
    name: 'Home',
    components: {
      Rank,
      TimeSeries,
      SnsMessage,
    }
}
</script>

<style>
.home-container {
  font-size: 0.9em;
  height: 100%;
  width: 100%;
  padding: 20px 25px;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 20px;
}

.home-container .item:nth-child(3) {
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 3;
}

.home-container .item {
  background-color: #1f2936;
  padding: 15px 20px;
  overflow: hidden;
  box-shadow: 1px 1px 10px 2px #a5def023;
  display: flex;
  flex-direction: column;
}

.home-container .item p{
  margin-bottom: 20px;
  margin-left: 10px;
}

.chart-wrapper {
  height: 88%;
  display: flex;
  justify-content: space-between;
}

</style>