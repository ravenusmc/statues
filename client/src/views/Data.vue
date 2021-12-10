<template>
  <div>
    <Intro />
    <hr />
    <section class='graph-one'>
      <GraphOneDiscussion />
      <GraphOne />
    </section>
  </div>
</template>

<script>
import Intro from '@/components/data/Intro.vue';
import GraphOneDiscussion from '@/components/data/GraphOneDiscussion.vue';
import GraphOne from '@/components/data/GraphOne.vue';

export default {
  name: 'Data',
  components: {
    Intro,
    GraphOneDiscussion,
    GraphOne,
  },
};
</script>

<style scoped>

.graph-one {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
}

</style>