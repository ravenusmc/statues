<template>
  <div>
    <section>
      <h1 class="center signup-title title-size font">Sign Up</h1>
      <form @submit="signup">
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="name"
            v-model="firstName"
            placeholder="First Name"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="name"
            v-model="lastName"
            placeholder="Last Name"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="email"
            v-model="email"
            placeholder="email"
          />
        </div>
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
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="password"
            v-model="confirmPassword"
            placeholder="Confirm Password"
          />
        </div>
        <button class="button is-success">Success</button>
      </form>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Form',
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      userName: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    signup(evt) {
      evt.preventDefault();
      if (this.firstName === '') {
        alert('First name must be entered');
      } else if (this.lastName === '') {
        alert('Last name must be entered');
      } else if (this.email === '') {
        alert('Email must be entered');
      } else if (this.userName === '') {
        alert('User name must be entered');
      } else if (this.password === '') {
        alert('Password must be entered');
      } else if (this.password !== this.confirmPassword) {
        alert('Passwords must be the same');
      } else if (this.password.length < 6) {
        alert('Password must be at least 6 characters long');
      } else {
        const payload = {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          userName: this.userName,
          password: this.password,
          confirmPassword: this.confirmPassword,
        };
        console.log(payload);
      }

      // this.$store.dispatch('common/login', { payload });
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
