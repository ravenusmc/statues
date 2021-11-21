<template>
  <div>
    <section>
      <h1 class="center signup-title title-size font">Sign Up</h1>
      <form @submit="login">
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="name"
            v-model="userName"
            placeholder="UserName"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="password"
            v-model="password"
            placeholder="Password"
          />
        </div>
        <button class="button is-success">Login</button>
      </form>
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Form',
  data() {
    return {
      userName: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['common/login']),
    login(evt) {
      evt.preventDefault();
      const payload = {
        userName: this.userName,
        password: this.password,
      };
      this.$store.dispatch('common/login', { payload });
    },
  },
};
</script>

<style scoped>
section {
  height: 80vh;
  margin: 5% 5% 5% 5%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.signup-title {
  text-transform: uppercase;
  font-weight: bold;
}
</style>
