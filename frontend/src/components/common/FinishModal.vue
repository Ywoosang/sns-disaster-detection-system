<template>
    <div class="modal">
        <div class="modal-item">
            <div class="modal-content">
                <div style="font-size: 0.9em">관리자에게 메일을 전송하였습니다.</div> 
            </div>
            <div class="modal-button">
                <button @click="closeFinishModal" style="background-color: rgba(69, 170, 242,0.8);">확인</button> 
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: 'FinishModal',
    methods: {
        ...mapMutations(["closeFinishModal"]),
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
    width: 360px;
    height: 22vh;
    z-index: 1001;
    opacity: none;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.modal .modal-item .modal-content {
    margin: 7vh 3vw 3vh 3vw;
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal .modal-item .modal-button {
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

@media (max-width: 767px) {
    .modal .modal-item{
        width: 80%;
        height: 22vh;
    }
}
</style>