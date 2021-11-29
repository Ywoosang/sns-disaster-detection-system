<template>
  <nav>
    <div class="menu">
      <ul>
        <li>
          <router-link to='/dashboard' class='btn' title="대시보드"><font-awesome-icon icon="fa-solid fa-house" /></router-link>
        </li>
        <li>
          <router-link to='/charts' class='btn' title="시간대별 재난 언급량"><font-awesome-icon icon="fa-solid fa-chart-line" /></router-link>
        </li>
        <li>
          <router-link to='/sns' class='btn' title="실시간 sns"><font-awesome-icon icon="fa-solid fa-comments" /></router-link>
        </li>
        <li>
          <div class="btn" title="관리자에게 메일 전송" @click="showModal"><font-awesome-icon icon="fa-solid fa-triangle-exclamation" /></div>
        </li>
        <li>
          <router-link to='/demo' class='btn' title="소개영상"><font-awesome-icon icon="fa-solid fa-video" /></router-link>
        </li>
        <li>
          <router-link to='/logs' class='btn' title="Ping test"><font-awesome-icon icon="fa-solid fa-tower-broadcast" /></router-link>
        </li>
        <li>
          <router-link to='/settings' class='btn' title="관리자 설정"><font-awesome-icon icon="fa-solid fa-gear" /></router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  name: 'NavBar',
  methods: {
    ...mapMutations(["showModal"])
  }
}
</script>

<style>
nav{
  background-color: #1f2936;
  min-width: 50px;
  overflow: auto;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  justify-content: space-between;
}

.menu {
  padding: 2px 10px;
}
.menu ul{
  list-style-type: none;
  padding-left: 0px;
}
.menu ul li{
  margin: 10px 0px;
}
.menu ul li .btn {
  display: block;
  color: rgba(255, 255, 255, 0.788);
  text-decoration: none;
  font-size: 25px;
}
.menu ul li .router-link-active {
  color: #17a9a8;
}
.menu ul li .btn:hover:not(.active) {
  color: #17a9a8;
}

.redo {
  margin: 15px auto;
}
.redo .redo-button {
  background-color: transparent;
  border: 0;
  outline: 0;
  font-size: 1.4em;
  color: rgba(255, 255, 255, 0.479);
}
</style>