<template>
  <div>
    <section :class="$style['section-area']">
      <div>
        <p>Select Discussion or Graph</p>
        <select @change="changeDisplay($event)" v-model="view">
          <option v-for="view in views" :key="view">
            {{ view }}
          </option>
        </select>
      </div>
      <div>
        <p>Select Graph Type: (Column or Line)</p>
        <select @change="changeGraphVersion($event)" v-model="graphVersion">
          <option v-for="graphVersion in graphVersions" :key="graphVersion">
            {{ graphVersion }}
          </option>
        </select>
      </div>
    </section>
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
    ...mapActions('discussion', [
      'changeBetweenDiscussionAndGraph',
      'changeGraphVersionAction',
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
    changeGraphVersion(event) {
      let graphVersion = this.graphVersion;
      const payload = {
        graphVersion,
      };
      this.changeGraphVersionAction({ payload });
    },
    changeGraphType() {
      this.typeOne = this.graphType.graphVersion;
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
  mounted() {
    this.typeOne = this.$store.getters['discussion/graphType'];
  },
};
</script>


<style lang="css" module>
.section-area {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-top: 50px;
  text-align: center;
}
</style>