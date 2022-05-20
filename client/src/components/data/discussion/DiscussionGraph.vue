<template>
  <div>
    <div>
      <select @change="changeDisplay($event)" v-model="view">
        <option>Select Discussion or Graph</option>
        <option v-for="view in views" :key="view">
          {{ view }}
        </option>
      </select>
    </div>
    <h1>GRAPH HERE</h1>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'DiscussionGraph',
  data() {
    return {
      view: 'Graph of Discussion Sentiment',
      views: ['Discussion', 'Graph of Discussion Sentiment'],
    };
  },
  methods: {
    ...mapActions('discussion', [
      'changeBetweenDiscussionAndGraph',
    ]),
    changeDisplay(event) {
      if (this.view == 'Discussion') {
        let show = true;
        const payload = {
          show,
				};
        this.changeBetweenDiscussionAndGraph({ payload });
      }
    },
  },
};
</script>


<style lang="css" module>
</style>