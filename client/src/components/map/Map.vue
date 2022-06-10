<template>
  <div>
    <h1>MAP</h1>
    <GChart
      :settings="{ packages: ['geochart'] }"
      type="GeoChart"
      :data="mapData"
      :options="chartOptions"
      ref="gChart"
      :resizeDebounce="100"
    />
  </div>
</template>

<script>
import { GChart } from "vue-google-charts";
import { mapGetters } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'Map',
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters('data', ['mapData']),
  },
  data() {
    return {
      typeOne: 'GeoChart',
      chartOptions: {
        title: 'Statues in North Vs South',
        region: 'US',
        displayMode: 'regions',
        resolution: 'provinces',
        legend: { position: 'top' },
        colors: ['#f24867'],
        height: 500,
        animation: {
          duration: 1000,
          easing: 'linear',
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
};
</script>

<style lang="css" module>
</style>