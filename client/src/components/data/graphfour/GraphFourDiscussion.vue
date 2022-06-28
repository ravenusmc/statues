<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Fourth Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
      First, this graph does not allow the user to change the dates. It's a
      graph that shows the top five states that removed statues after
      Charlottesville. What is surprising to me is that the data shows that the
      main state that removed statues was Texas. I did not expect this. I
      actually thought that Georgia would have the most removed or maybe North
      Carolina. Texas just seemes way to conservative for me. It really makes me
      wonder why did Texas decide to pull so many statues down? Was it done on
      the local or state levels or was it mass protest?
    </p>
    <br />
    <p>
      This graph will have a drill down to see which statues were removed. As
      with the other graphs, simply click on the bar you want to drill down on
      and a table will appear showing you the data.
    </p>
    <form class='discussion-form' @submit.prevent="selectedGraphForDiscussion">
      <h6 class='discussion_title'>Discuss Graph Four</h6>
      <input :value="4" hidden />
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