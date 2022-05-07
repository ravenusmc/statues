<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Fifth Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the left...</span>
      <span class="responsive-phrase-small">The above graph...</span>
    </p>
    <br />
    <p>
      The fifth graph I think is one of those graphs that you can quickly look
      at and see the effects of when culture starts to change. What I mean is
      that Confederate statues had been around, in some cases, over a 100 years.
      In the early 2010's we had the rise of the Black Lives Matter movement.
      This is where we can start to see some statues being taken down. But it
      was not until 2020, with the death of George Floyd, that the removal of
      statues peaked. The graph clearly shows this happening. Then the next
      year, in 2021, the amount of statues which were being removed dropped once
      again. I'd say that each year going forward the statues being removed will
      drop until it make be either 0,1 or 2 per year.
    </p>
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph Five</h6>
      <input :value="5" hidden />
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