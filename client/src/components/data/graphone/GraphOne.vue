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