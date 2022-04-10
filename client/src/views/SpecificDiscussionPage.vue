<template>
  <div>
    <h1>Welcome {{ userObject.username }}</h1>
    <section>
      <div>
        <form @submit.prevent="submitDiscussion">
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
      </div>
      <div></div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'SpecificDiscussionPage',
  computed: {
    ...mapGetters('session', ['userObject']),
  },
  methods: {
    ...mapActions(['common/login']),
    submitDiscussion(evt) {
      // evt.preventDefault();
      // const payload = {
      //   userName: this.userName,
      //   password: this.password,
      // };
      // this.$store.dispatch('common/login', { payload });
    },
  },
};
</script>