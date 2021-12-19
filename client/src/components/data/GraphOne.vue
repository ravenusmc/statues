<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="firstGraphDataSetInitial"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'GraphOne',
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters('data', ['firstGraphDataSetInitial']),
  },
  data() {
    return {
      typeOne: 'ColumnChart',
      chartOptionsOne: {
        title: 'Statues in North Vs South',
        legend: { position: 'top' },
        colors: ['#05ce78'],
        height: 500,
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

<style scoped>
</style>