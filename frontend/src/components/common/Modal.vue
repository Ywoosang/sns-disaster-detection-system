<template>
  <div class="modal">
    <div class="modal-item">
      <div class="modal-content">
        <div
          class="modal-icon"
          style="font-size: 5.5em; color: rgba(255, 218, 55, 0.801)"
        >
          <font-awesome-icon icon="fa-solid fa-circle-exclamation" />
        </div>
        <div class="modal-text">
          <div style="font-size: 1.5em; margin-bottom: 20px">
            이상 상태 알림
          </div>
          <div style="font-size: 0.9em">재난 상황으로 추정됩니다.</div>
        </div>
      </div>
      <div class="modal-button">
        <button
          @click="sendMail"
          style="background-color: rgba(252, 92, 101, 0.8)"
        >
          관리자에게 메일보내기
        </button>
        <button
          @click="closeModal"
          style="background-color: rgba(69, 170, 242, 0.8)"
        >
          창 닫기
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
import { postMail } from '../../api/request'

export default {
  name: "Modal",
  methods: {
    ...mapMutations(["closeModal", "showFinishModal"]),
    async sendMail() {
      try {
        const mailText = localStorage.getItem("mailText");
        const manager =  localStorage.getItem("manager");
        console.log(manager)
        console.log(mailText)
        if(!manager) return alert('설정 > 관리자를 설정해 주세요.');
        if(!mailText) return alert('설정 > 메일 본문을 설정해 주세요.')
        await postMail(manager,mailText)
      } catch (error) {
        if (error.response) {
          console.log(error.response.message);
        }
      }
      this.closeModal();
      this.showFinishModal();
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100%;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal .modal-item {
  background-color: #263850;
  width: 400px;
  height: 50vh;
  z-index: 1001;
  opacity: none;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal .modal-item .modal-content {
  flex: 5;
  display: flex;
  flex-direction: column;
  margin: 2vh 5vw;
  align-items: center;
  justify-content: space-around;
  align-content: space-between;
}

.modal .modal-item .modal-button {
  flex: 1;
  display: flex;
  justify-content: space-around;
  width: 250px;
}

.modal .modal-item .modal-button button {
  height: 5vh;
  max-height: 30px;
  border: 0;
  outline: 0;
  font-size: 0.9em;
  color: rgba(255, 255, 255, 0.849);
  border-radius: 0.3em;
}

@media (max-width: 767px) {
  .modal .modal-item {
    width: 90%;
    height: 50vh;
    z-index: 1001;
    opacity: none;
  }
}
</style>