<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Third Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
      Now this graph started to get me really thinking that something is going
      on here with this data. The amount of statues that are not from the North
      is huge. Select just about any Southern state and the data that I have
      does not show any statues of the North. It's like the North does not even
      have any memories of the war. With the South, the number of statues that
      they have really seems to show that they think of the war very fondly.
    </p>
    <br />
    <p>
      The South lost the war though! Yet, one would not be able to tell from any
      of these graphs. This graph works similar to the others except one is able
      to select a state as well as a time period. The data that comes back shows
      three columns - the amount of statues that are for the North, South and
      that have Side being blank - that is Not Applicable. Again, you'll almost
      think that the graph is broken because there appear to hardly be any
      statues for the North.
    </p>
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph Three</h6>
      <input :value="3" hidden />
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
      this.getDisscusionData({ payload });
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