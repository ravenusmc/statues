<template>
  <div>
    <section>
      <Pictures class="pictures" />
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

@media only all and (max-width: 900px) {
  section {
    grid-template-columns: 1fr;
  }

  .pictures {
    display: none;
  }
}
</style>
