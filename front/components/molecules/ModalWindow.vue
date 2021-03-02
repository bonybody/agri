<template>
  <div class="modal-window" v-show="show">
    <div class="modal-window__content">
      <slot></slot>
      <div class="modal-window__close">
        <app-button @myClick="$emit('close-modal')">閉じる</app-button>
      </div>
    </div>
  </div>
</template>

<script>
import AppButton from "~/components/atoms/buttons/AppButton";
export default {
  name: "ModalWindow",
  components: {AppButton},
  props: {
    show: {
      type: false,
      default: false,
    }
  }
}
</script>

<style scoped lang="scss">
.modal-window {
  /*　要素を重ねた時の順番　*/
  z-index: 1;

  /*　画面全体を覆う設定　*/
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);

  /*　画面の中央に要素を表示させる設定　*/
  display: flex;
  align-items: center;
  justify-content: center;

  &__content {
    width: 300px;
    height: 200px;
    background-color: $main-background-color;
  }
  &__close {
    height: 35px;
    width: 100px;
  }
}
</style>