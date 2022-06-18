<template>
  <div>
    <h1>Map Of Statues By Year</h1>
    <h6>Current Year: {{ mapYear }}</h6>
    <section>
      <div>
        <h3>Change Year, a year at a time:</h3>
        <svg
          @click="changeYear('increaseYear')"
          xmlns="http://www.w3.org/2000/svg"
          width="30"
          height="30"
          fill="currentColor"
          class="bi bi-arrow-up-square-fill"
          viewBox="0 0 16 16"
          :class="$style['spacing-fix']"
        >
          <path
            d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"
          />
        </svg>
        <svg
          @click="changeYear('decreaseYear')"
          xmlns="http://www.w3.org/2000/svg"
          width="30"
          height="30"
          fill="currentColor"
          class="bi bi-arrow-down-square-fill"
          viewBox="0 0 16 16"
        >
          <path
            d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"
          />
        </svg>
      </div>
      <div>
        <form @submit="submitYear">
          <h3>Or enter year to go to:</h3>
          <label for="yearOne">Enter Year (1854-2017):</label>
          <input
            type="number"
            id="year"
            v-model="year"
            name="year"
            min="1854"
            max="2017"
          />
          <button class="button is-success font">Submit</button>
        </form>
      </div>
    </section>
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
import { GChart } from 'vue-google-charts';
import { mapGetters, mapActions } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'Map',
  components: {
    GraphCard,
  },
  computed: {
    ...mapGetters('data', ['mapData', 'mapYear']),
  },
  data() {
    return {
      year: 1854,
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
  methods: {
    ...mapActions('data', ['fetchMapData']),
    submitYear(evt) {
      evt.preventDefault();
      const payload = {
        year: this.year
      };
      this.fetchMapData({ payload });
    },
    changeYear(direction) {
      let year = 1854
      if (direction === 'increaseYear'){
        year = Number(this.mapYear) + 1
      }else {
        year = Number(this.mapYear) - 1
      }
      year = year.toString()
      const payload = {
        year
      }
      this.fetchMapData({ payload });
    }
  },
};
</script>

<style lang="css" module>
.spacing-fix {
  margin-right: 10px;
}
</style>