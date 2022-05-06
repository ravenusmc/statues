<template>
  <div>
    <GraphCard
      :typeOne="typeOne"
      :data="removedStatuesByYearsData"
      :options="chartOptionsOne"
    />
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph Five</h6>
      <input :value="5" hidden />
      <button type="submit" class="btn btn-outline-dark">
        Go to Discussion
      </button>
    </form>
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
  methods: {
    selectedGraphForDiscussion(evt) {
      let selectedValue = evt.target[0]._value;
      const payload = {
        selectedGraphDiscussion: selectedValue,
      };
      this.$store.dispatch('discussion/getDisscusionData', { payload });
    },
  },
};
</script>