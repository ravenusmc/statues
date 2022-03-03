<template>
  <div>
    <!-- <GraphCard
      :typeOne="typeOne"
      :data="removedStatuesByYearsData"
      :options="chartOptionsOne"
    /> -->
    {{removedStatuesByYearsData}}
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
    ...mapGetters('data', ['removedStatuesByYearsData']),
  },
  data() {
    return {
      typeOne: 'LineChart',
      chartOptionsOne: {
        title: 'Last Ten Years of Statue Removal',
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