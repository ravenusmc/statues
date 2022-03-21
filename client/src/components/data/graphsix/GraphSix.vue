<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="sixthGraphDataSet"
      :options="chartOptionsOne"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'GraphSix',
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters('data', ['sixthGraphDataSet']),
  },
  data() {
    return {
      typeOne: 'ColumnChart',
      chartOptionsOne: {
        title: 'Statue Type by State and Time',
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