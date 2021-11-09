<template>
  <div>
    <section>
      <Pictures />
      <Form />
    </section>
  </div>
</template>

<script>
import Pictures from '@/components/signup/Pictures.vue';
import Form from '@/components/signup/Form.vue';

export default {
  name: 'SignUp',
  components: {
    Pictures,
    Form,
  },
};
</script>

<style scoped>
section {
  height: 95vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
