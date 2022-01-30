<template>
  <div>
    <section>
      <h2 class="center signup-title title-size font">Login</h2>
      <h1 v-if="userNotFound" class="center font alert">
        User is not found, Please
        <a><router-link class="alert" to="/sign_up">sign up.</router-link></a>
      </h1>
      <h1 v-if="passwordNoMatch" class="center font alert">
        Password is Invalid
      </h1>
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
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Form',
  computed: {
    ...mapGetters('common', ['userNotFound', 'passwordNoMatch']),
  },
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

@media only all and (max-width: 900px) {
  section {
    margin-top: -100px;
  }
}
</style>
