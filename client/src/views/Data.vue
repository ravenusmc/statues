<template>
  <div>
    <Intro />
    <hr>
    <GraphOne />
  </div>
</template>

<script>
import Intro from '@/components/data/Intro.vue';
import GraphOne from '@/components/data/GraphOne.vue';

export default {
  name: 'Data',
  components: {
    Intro,
    GraphOne, 
  },
};
</script>

<style scoped>
</style>