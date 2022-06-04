<template>
  <div>
    <div :class="$style['section-area']">
      <p>Select Discussion or Graph</p>
      <select @change="changeDisplay($event)" v-model="view">
        <option v-for="view in views" :key="view">
          {{ view }}
        </option>
      </select>
    </div>
    <div :class="$style['section-area']">
      <select @change="changeDisplay($event)" v-model="graphVersion">
        <option>Select Graph Type: (Column or Line)</option>
        <option v-for="graphVersion in graphVersions" :key="graphVersion">
          {{ graphVersion }}
        </option>
      </select>
    </div>
    <GraphCard
      :typeOne="typeOne"
      :data="sentiment_graph_data"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'DiscussionGraph',
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters('discussion', ['sentiment_graph_data', 'graphType']),
  },
  data() {
    return {
      view: 'Graph of Discussion Sentiment',
      views: ['Discussion', 'Graph of Discussion Sentiment'],
      graphVersion: 'ColumnChart',
      graphVersions: ['ColumnChart', 'LineChart'],
      typeOne: '',
      chartOptionsOne: {
        title: 'Graph of Sentiment for each Discussion',
        legend: { position: 'top' },
        colors: ['#f24867'],
        height: 600,
        hAxis: {
          title: 'Discussion',
        },
        vAxis: {
          title: 'Sentiment',
          viewWindow: {
            min: -1,
            max: 1,
          },
        },
      },
    };
  },
  methods: {
    ...mapActions('discussion', ['changeBetweenDiscussionAndGraph']),
    changeDisplay(event) {
      if (this.view == 'Discussion') {
        let show = true;
        const payload = {
          show,
        };
        this.changeBetweenDiscussionAndGraph({ payload });
      }
    },
    changeGraphType() {
      console.log('Hi');
      console.log(this.graphType)
      this.typeOne = this.graphType;
    },
  },
  watch: {
    graphType: {
      handler(value) {
        if (value) {
          this.changeGraphType();
        }
      },
      immediate: true,
    },
  },
};
</script>


<style lang="css" module>
.section-area {
  margin-top: 50px;
  text-align: center;
}
</style>