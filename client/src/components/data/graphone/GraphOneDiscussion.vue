<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">First Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
      This graph allows the user to see the count of statues in the North, South
      and areas that I've labeled "Not Applicable." The user is able to select a
      time period and see how the number of statues changed with time. The user
      is also able to click on one of the columns to drill down into the data.
      The window that then appears will allow the user to see more information
      on the statues that make up that data.
    </p>
    <br />
    <p>
      There's one thing that stands out to me on the graph. The South always
      appears to have more statues than the North. The North won the war. I
      almost would have thought that the North would have had more statues up
      until about 1890. That is very clearly not the case. From the start,
      according to the data, the South had way more statues than the North did.
      The South, from the start, appears to have been much more willing to pay
      tribute to the fallen than the North. Still this does not make much sense
      to me. The Lost Cause Myth I believe was developed towards the end of the
      19th century. I'd almost expect to have more statues in the North up until
      that point.
    </p>
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph One</h6>
      <input :value="1" hidden />
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