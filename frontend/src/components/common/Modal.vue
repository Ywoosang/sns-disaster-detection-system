<template>
    <div class="modal">
        <div class="modal-item">
            <div class="modal-content">
                <div class="modal-icon" style="font-size: 5.5em; color: rgba(255, 218, 55, 0.801)"><font-awesome-icon icon="fa-solid fa-circle-exclamation" /></div>
                <div class="modal-text">
                    <div style="font-size: 1.5em; margin-bottom: 20px">이상 상태 알림</div>
                    <div style="font-size: 0.9em">재난 상황으로 추정됩니다.</div> 
                </div>
            </div>
            <div class="modal-button">
                <button @click='sendMail' style="background-color: rgba(252, 92, 101,0.8);">관리자에게 메일보내기</button>
                <button @click="closeModal" style="background-color: rgba(69, 170, 242,0.8);">창 닫기</button> 
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapMutations } from "vuex";

export default {
    name: 'Modal',
    methods: {
        ...mapMutations(["closeModal", "showFinishModal"]),
        async sendMail() {
            try{
                await axios.post('http://localhost:8080/api/mail',{
                    message : '(키워드)의 언급량이 급증했습니다.'
                });  
            }catch(error){
                if(error.response){
                    console.log(error.response.message);
                } 
            } 
            this.closeModal();
            this.showFinishModal();
        }
    }
}
</script>

<style scoped>
.modal{
    position: fixed;
    top:0;
    left:0;
    width: 100vw;
    height: 100%;
    z-index: 1000;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal .modal-item{
    background-color: #263850;
    width: 400px;
    height: 50vh;
    z-index: 1001;
    opacity: none;
    display: flex;
    flex-direction: column;
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
    margin: 0 5vw 5vh 5vw; 
    display: flex;
    justify-content: space-around;
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

 
</style>