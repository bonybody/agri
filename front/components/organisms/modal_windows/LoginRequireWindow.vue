<template>
  <div class="login-window">
    <modal-window
        :show="showModal"
        :buttons-length="modalButtons"
        @close-modal="$emit('close-modal')">
      <template v-slot:heading>ログインが必要です</template>
      <template v-slot:text>
        この操作を行うにはユーザーのログインが必要です。
      </template>
      <template #[modalButtonSlotNames(1)]>
        <app-link-button :link="{ path: '/login' }">ログイン</app-link-button>
      </template>
    </modal-window>
  </div>
</template>

<script>
import ModalWindow from "@/components/molecules/ModalWindow";

export default {
  name: "LoginRequireWindow",
  components: {ModalWindow},
  data() {
    return {
      modalButtons: 1
    }
  },
  props: {
    showModal: {
      type: Boolean,
      require: true
    }
  },
  computed: {
    loggedIn() {
      return this.loggedIn()
    }
  },
  methods: {
    modalButtonSlotNames(number) {
      return 'buttons' + number
    },
  }

}
</script>

<style scoped>

</style>