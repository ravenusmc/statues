<template>
  <div>
    <section>
      <h1 class='center signup-title title-size font'>Sign Up</h1>
      <form>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="name"
            placeholder="Name"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="email"
            placeholder="email"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="password"
            placeholder="Password"
          />
        </div>
        <div class="field">
          <input
            class="input is-primary is-rounded"
            type="password"
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
