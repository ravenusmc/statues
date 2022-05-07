<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Second Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the left...</span>
      <span class="responsive-phrase-small">The above graph...</span>
    </p>
    <br />
    <p>
      This graph allows the user to see the states with the most statues in a
      given range of years. Like the first graph, the user is able to select a
      time period and see how the number of statues, in the top five states,
      changed with time. Again, the user is also able to click on one of the
      columns to drill down into the data. The window that then appears will
      allow the user to see more information on the statues that make up that
      data.
    </p>
    <br />
    <p>
      Like the first graph, there's one thing that stands out to me. The South,
      once again, appears to be the place with the most statues. The initial
      date range, 1854 - 2017, has the top five states all being in the south.
      I've played around with the date ranges and I always five that the states
      listed are all in the south. I've yet to find a date range which has at
      least one northern state. As I move forward on this project it really
      appears to me that the way that the South remembered the Civil War
      compared to the North was very different. I'd really like to dig down into
      why the South had so many more statues - they lost the war! Why have so
      many statues to something that you lost - unless you try and change the
      way that event is remembered. Maybe the Lost Cause explanation has
      something to do with it?
    </p>
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph Two</h6>
      <input :value="2" hidden />
      <button type="submit" class="btn btn-outline-dark">
        Go to Discussion
      </button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'GraphOneDiscussion',
   methods: {
    ...mapActions('discussion', ['getDisscusionData']),
    selectedGraphForDiscussion(evt) {
      let selectedValue = evt.target[0]._value;
      const payload = {
        selectedGraphDiscussion: selectedValue,
      };
      this.getDisscusionData({ payload })
    },
  },
};
</script>

<style scoped>
.responsive-phrase-large {
  display: block;
}

.responsive-phrase-small {
  display: none;
}

.graph-discussion {
  margin: 0 10% 0 10%;
}

.heading-title {
  font-weight: bolder;
  font-size: 2em;
  text-transform: uppercase;
  margin-bottom: 15px;
}

/* Responsive media quries */
@media only all and (max-width: 999px) {
  .responsive-phrase-large {
    display: none;
  }

  .responsive-phrase-small {
    display: block;
  }
}
</style>