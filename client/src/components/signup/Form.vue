<template>
  <div>
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
  </div>
</template>

<script>
export default {
  name: 'Form',
};
</script>

<style scoped>
</style>
