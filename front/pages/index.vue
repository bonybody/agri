<template>
  <div class="container">
    <div>
      <Logo />
      <h1 class="title">
        takasima
      </h1>
      <div class="links">
        <a
          href="https://nuxtjs.org/"
          target="_blank"
          rel="noopener noreferrer"
          class="button--green"
        >
          <kuro-334/>
        </a>
        <nuxt-link to="/login" class="button--green">
          ログイン
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
import kuro334 from '../components/test/kuro334.vue';
export default {
  auth: "guest",
  components: { kuro334 },
  mounted() {
    console.log(this.$auth.loggedIn);
  },
}
</script>

<style lang="scss">
.container {
  //background-color: $primary-color;
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
