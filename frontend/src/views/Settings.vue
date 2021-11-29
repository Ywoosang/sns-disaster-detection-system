<template>
  <div class="settings-container">
    <div class="content-wrapper">
      <p style="margin-bottom: 40px; margin-top: 40px" class="setting-manager">관리자 설정</p>
      <p style="margin-bottom: 20px">
        이상 상태 시 메일을 전송할 관리자를 설정하세요.
      </p>
      <div class="info">현재 관리자 이메일: {{ manager }}</div>
      <div class="info" v-if="newManager">변경할 이메일: {{ newManager }}</div>
      <div class="input-wrapper">
        <input type="email" v-model="newManager" placeholder="이메일 주소" />
        <button @click="setManager">설정</button>
      </div>
      <p style="margin-bottom: 20px">
        이상 상태 시 전송할 메일의 본문을 설정하세요.
      </p>
      <div class="info">현재 관리자에게 전송할 메일 본문: {{ mailText }}</div>
      <div class="info"  v-if="newMailText">변경할 메일 본문: {{ newMailText }}</div>
      <div class="input-wrapper">
        <textarea
          placeholder="내용을 입력하세요."
          v-model="newMailText"
          rows="5"
          cols="30"
        />
        <button @click="setMailText">설정</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            manager: "없음",
            mailText: "없음",
            newManager:'',
            newMailText: '',
        }
    },
    created(){
        this.manager = localStorage.getItem("manager") || '설정된 이메일이 없습니다.';
        this.mailText = localStorage.getItem("mailText") || '설정된 메일 본문이 없습니다.';
    },
    methods : {
        setManager(){
            const re =/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
            if (this.newManager == '' || !re.test(this.newManager)) {
                return alert("올바른 이메일 주소를 입력하세요")
            }
            localStorage.removeItem("manager");
            localStorage.setItem("manager", this.newManager);
            this.manager = this.newManager
            this.newManager = ''
        },
        setMailText(){
            localStorage.removeItem("mailText");
            localStorage.setItem("mailText", this.newMailText);
            this.mailText = this.newMailText;
            this.newMailText = ''
        },
    }
}
</script> 

<style scoped>
.settings-container {
  overflow: auto;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.settings-container .content-wrapper {
  width: 40%;
  min-width: 400px;
  min-height: 450px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #1f2936;
  box-shadow: 1px 1px 10px 2px #a5def023;
}
.info {
  font-size: 0.9em;
  max-width: 300px;
  overflow: auto;
  margin-bottom: 15px;
  min-height: 25px;
}
.input-wrapper {
  display: flex;
  justify-content: space-around;
  margin-bottom: 35px;
}

.settings-container input {
  font-size: 0.9rem;
  padding-left: 10px;
  padding-right: 10px;
  border: none;
  margin-right: 10px;
  size: 40;
  text-align: justify;
  overflow: auto;
}
.settings-container input:focus {
  outline: none;
}

.settings-container textarea {
  font-size: 0.9rem;
  padding-left: 10px;
  padding-right: 10px;
  border: none;
  margin-right: 10px;
  text-align: justify;
  overflow: auto;
}
.settings-container textarea:focus {
  outline: none;
}

.settings-container button {
  border: none;
  border-radius: 4px;
  text-align: center;
  height: 25px;
  color: rgba(255, 255, 255, 0.849);
  background-color: rgb(39, 60, 87);
}

@media (max-width: 767px) {
  .settings-container .content-wrapper {
    width: 80%;
    min-width: 0;
    min-height: 0;
    padding: 0 20px;
  }
  .settings-container button {
    width: 40px;
    margin-top: 10px;
  }
  .settings-container input {
    margin-right: 0;
  }
  .settings-container textarea {
    margin-right: 0;
  }
  .input-wrapper {
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }
  .setting-manager {
    margin-bottom: 25px !important;
  }
}
</style>