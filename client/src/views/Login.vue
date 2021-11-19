<template>
  <div>
    <section>
      <LoginPicture />
      <LoginForm />
    </section>
  </div>
</template>

<script>
import LoginPicture from '@/components/login/LoginPicture.vue';
import LoginForm from '@/components/login/LoginForm.vue';

export default {
  name: 'Login',
  components: {
    LoginPicture,
    LoginForm,
  },
};
</script>

<style scoped>
section {
  height: 95vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media only all and (max-width: 900px) {
  section {
    grid-template-columns: 1fr;
  }

  .pictures {
    display: none;
  }
}
</style>
