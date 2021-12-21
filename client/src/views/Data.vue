<template>
  <div>
    <Intro />
    <hr />
    <section class="graph-one">
      <GraphOneDiscussion />
      <div>
        <GraphOne />
        <FormOne />
      </div>
    </section>
  </div>
</template>

<script>
import Intro from '@/components/data/Intro.vue';
import GraphOneDiscussion from '@/components/data/GraphOneDiscussion.vue';
import GraphOne from '@/components/data/GraphOne.vue';
import FormOne from '@/components/data/FormOne.vue';

export default {
  name: 'Data',
  components: {
    Intro,
    GraphOneDiscussion,
    GraphOne,
    FormOne,
  },
};
</script>

<style scoped>
.graph-one {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
}
</style>