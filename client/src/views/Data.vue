<template>
  <div>
    <Intro />
    <hr />
    <section class="graph-area">
      <GraphOneDiscussion />
      <div>
        <GraphOne />
        <FormOne />
      </div>
    </section>
    <hr />
    <section class="graph-area">
      <div>
        <GraphTwo />
        <FormTwo />
      </div>
      <GraphTwoDiscussion />
    </section>
    <hr />
    <section class="graph-area">
      <GraphThreeDiscussion />
      <div>
        <GraphThree />
        <FormThree />
      </div>
    </section>
    <hr />
    <section class="graph-area">
      <GraphFourDiscussion />
      <div>
        <GraphFour />
      </div>
    </section>
    <section class="graph-area">
      <div>
        <GraphFive />
      </div>
      <GraphFiveDiscussion />
    </section>
  </div>
</template>

<script>
import Intro from '@/components/data/Intro.vue';
import GraphOneDiscussion from '@/components/data/graphone/GraphOneDiscussion.vue';
import GraphOne from '@/components/data/graphone/GraphOne.vue';
import FormOne from '@/components/data/graphone/FormOne.vue';
import GraphTwoDiscussion from '@/components/data/graphtwo/GraphTwoDiscussion.vue';
import FormTwo from '@/components/data/graphtwo/FormTwo.vue';
import GraphTwo from '@/components/data/graphtwo/GraphTwo.vue';
import GraphThreeDiscussion from '@/components/data/graphthree/GraphThreeDiscussion.vue';
import FormThree from '@/components/data/graphthree/FormThree.vue';
import GraphThree from '@/components/data/graphthree/GraphThree.vue';
import GraphFourDiscussion from '@/components/data/graphfour/GraphFourDiscussion.vue';
import GraphFour from '@/components/data/graphfour/GraphFour.vue';
import GraphFiveDiscussion from '@/components/data/graphfive/GraphFiveDiscussion.vue';
import GraphFive from '@/components/data/graphfive/GraphFive.vue';

export default {
  name: 'Data',
  components: {
    Intro,
    GraphOneDiscussion,
    GraphOne,
    FormOne,
    GraphTwoDiscussion,
    FormTwo,
    GraphTwo,
    GraphThreeDiscussion,
    FormThree,
    GraphThree,
    GraphFourDiscussion,
    GraphFour,
    GraphFiveDiscussion,
    GraphFive,
  },
};
</script>

<style scoped>
.graph-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
}
</style>