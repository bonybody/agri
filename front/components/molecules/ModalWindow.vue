<template>
  <div class="modal-window" v-show="show">
    <div class="modal-window__content">
      <div class="modal-window__heading">
        <app-heading>
          <slot name="heading"></slot>
        </app-heading>
      </div>
      <div class="modal-window__text">
        <slot name="text"></slot>
      </div>
      <div class="modal-window__separate">
        <app-separation/>
      </div>
      <div v-for="button in buttonsLength" class="modal-window__buttons">
        <slot :name="'buttons' + button"></slot>
      </div>
      <div class="modal-window__close">
        <app-button @myClick="$emit('close-modal')">閉じる</app-button>
      </div>
    </div>
  </div>
</template>

<script>
import AppButton from "~/components/atoms/buttons/AppButton";
import AppHeading from "@/components/atoms/headings/AppHeading";
import AppSeparation from "@/components/atoms/separations/AppSeparation";

export default {
  name: "ModalWindow",
  components: {AppSeparation, AppHeading, AppButton},
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    buttonsLength: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style scoped lang="scss">
.modal-window {
  /*　要素を重ねた時の順番　*/
  z-index: 10000;

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
    border-radius: $box-border-radius;
    box-sizing: border-box;
    padding: $medium-parts-margin;
    width: 400px;
    background-color: $main-background-color;
  }

  &__heading {
    text-align: center;
    margin-bottom: $medium-parts-margin;
  }

  &__text {
    text-align: center;
    margin-bottom: $semi-large-margin;
  }

  &__separate {
    margin-bottom: $medium-parts-margin;
  }

  &__buttons {
    height: 35px;
    width: 200px;
    margin: 0 auto $medium-parts-margin auto;
  }

  &__close {
    height: 35px;
    width: 200px;
    margin: 0 auto;
  }
}
</style>