<template>
  <div>
    <section>
      <Pictures />
    </section>
  </div>
</template>

<script>
import Pictures from '@/components/signup/Pictures.vue';

export default {
  name: 'SignUp',
  components: {
    Pictures,
  },
};
</script>

<style scoped>
section {
  border: 2px solid red;
  height: 90vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
