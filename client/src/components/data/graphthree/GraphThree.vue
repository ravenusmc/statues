<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="thirdGraphDataSet"
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
    ...mapGetters('data', ['thirdGraphDataSet']),
  },
  data() {
    return {
      typeOne: 'ColumnChart',
      chartOptionsOne: {
        title: 'Statues by Single State',
        legend: { position: 'top' },
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