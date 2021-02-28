<template>
  <label :for="name" class="input-image">
    <div class="input-image__label-icon">画像</div>
    <input class="input-image__input" type="file" :name="name" ref="preview" @change="uploadFile" hidden>
    <img class="input-image__img" v-if="previewUrl" :src="previewUrl" alt="アップロード画像プレビュー">
  </label>
</template>

<script>
import input from "~/mixins/input";

export default {
  name: "AppInputImage",
  mixins: [input],
  data() {
    return {
      previewUrl: ''
    }
  },
  props: {
    name: {
      type: String,
      require: true
    },
    value: {
      type: String,
      require: true
    }
  },
  methods: {
    uploadFile() {
      const file = this.$refs.preview.files[0];
      this.previewUrl = URL.createObjectURL(file)
      this.$emit('changeValue', file)
      this.$refs.preview.value = "";
    }
  }
}
</script>

<style scoped lang="scss">
.input-image {
  display: block;
  position: relative;
  width: 100%;
  height: 100%;
  background-color: $weak-font-color;
  @include border-radius-box();

  &__input {

  }

  &__img {
    position: relative;
    z-index: 2;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &__label-icon {
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    text-align: center;
    height: 1em;
    margin: auto;
  }
}
</style>