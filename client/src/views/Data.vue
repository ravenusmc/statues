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
    <hr />
    <section class="graph-area">
      <div>
        <GraphFive />
      </div>
      <GraphFiveDiscussion />
    </section>
    <hr />
    <section class="graph-area">
      <GraphSixDiscussion />
      <div>
        <GraphSix />
        <FormSix />
      </div>
    </section>
    <hr />
    <section class="graph-area">
      <Map />
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
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
import GraphSixDiscussion from '@/components/data/graphsix/GraphSixDiscussion.vue';
import FormSix from '@/components/data/graphsix/FormSix.vue';
import GraphSix from '@/components/data/graphsix/GraphSix.vue';
import Map from '@/components/map/Map.vue';


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
    GraphSixDiscussion,
    FormSix,
    GraphSix,
    Map,
  },
  data() {
    return {
      years: {
        yearOne: '',
        yearTwo: '',
      },
      graphNumber: 0,
    };
  },
  methods: {
    ...mapActions('data', ['fetchNorthSouthByYear']),
    submitForm(evt) {
      evt.preventDefault();
      console.log(this.graphNumber);
      let yearOne = Number(this.years.yearOne);
      let yearTwo = Number(this.years.yearTwo);
      if (yearOne >= yearTwo) {
        alert('Year One must be less than year two.');
      } else if (yearTwo <= yearOne) {
        alert('Year Two must be greater than year one');
      } else if (yearOne === yearTwo) {
        alert('The years cannot be the same.');
      } else {
        const payload = {
          yearOne,
          yearTwo,
        };
        this.fetchNorthSouthByYear({ payload });
      }
    },
  },
};
</script>

<style scoped>
.graph-area {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
}
</style>