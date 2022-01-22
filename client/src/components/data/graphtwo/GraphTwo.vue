<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="secondGraphDataSetInitial"
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
    ...mapGetters('data', ['secondGraphDataSetInitial']),
  },
  data() {
    return {
      typeOne: 'ColumnChart',
      chartOptionsOne: {
        title: 'Top Five States with Most Statues by Year',
        legend: { position: 'top' },
        colors: ['#05ce78'],
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