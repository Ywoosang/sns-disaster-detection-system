<template>
  <div class="demo-container">
      <div class="video-wrapper">
        <p>소개영상</p>
        <video src="">안녕</video>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.demo-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.video-wrapper {
    background-color: #1f2936;
    box-shadow: 1px 1px 10px 2px #a5def023;
    padding: 10px 30px 30px 30px;
}
.video-wrapper p {
    text-align: center;
}
.video-wrapper video{
    width: 600px;
    height: 450px;
    background-color: grey;
}

@media (max-width: 767px) {
    .video-wrapper {
        width: 80%;
        padding: 10px 10px 30px 10px;
    }
    .video-wrapper video{
        width: 100%;
        height: 100%;
    }
}
</style>