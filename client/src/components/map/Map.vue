<template>
  <div>
    <Modal
      :data="drillDownData"
      :showModal="showModal"
      :modalTitle="modalTitle"
      @close-modal="update"
    />
    <section :class="$style['year-section']">
      <h1 :class="$style['map-title']">Map Of Statues By Year</h1>
      <h3>
        Current Year:
        <span :class="$style['selected-year']">{{ mapYear }}</span>
      </h3>
      <div :class="$style['single-year-change']">
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
          <h3 :class="$style['subtitle-fix']">Or enter year to go to:</h3>
          <label :class="$style['label-fix']" for="yearOne"
            >Enter Year (1854-2017):</label
          >
          <input
            type="number"
            id="year"
            v-model="year"
            name="year"
            min="1854"
            max="2017"
            :class="$style['spacing-fix']"
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
      :events="chartEvents"
    />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts';
import Modal from '@/components/data/Modal.vue';
import { mapGetters, mapActions } from 'vuex';
import GraphCard from '@/components/Graphs/GraphCard.vue';

export default {
  name: 'Map',
  components: {
    GraphCard,
    Modal,
  },
  computed: {
    ...mapGetters('data', ['mapData', 'mapYear', 'drillDownData']),
  },
  data() {
    return {
      modalTitle: '',
      showModal: false,
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
      chartEvents: {
        select: () => {
          // console.log(this.mapData);
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          let row = selection.row + 1;
          let selectedRow = this.mapData[row];
          let state = '';
          if (selectedRow[0].length > 2) {
            state = selectedRow[0].slice(3);
          } else {
            state = selectedRow[0];
          }
          const payload = {
            state,
            year: this.mapYear,
          };
          this.$store.dispatch('data/fetchMapDrillDownData', {
            payload,
          });
          if (this.mapYear === 1854) {
            this.modalTitle = `Drilldown Information for ${state} in ${this.mapYear}`;
          } else {
            this.modalTitle = `Drilldown Information for ${state} between 1854 and ${this.mapYear}`;
          }
          this.showModal = true;
        },
      },
    };
  },
  methods: {
    ...mapActions('data', ['fetchMapData']),
    submitYear(evt) {
      evt.preventDefault();
      const payload = {
        year: this.year,
      };
      this.fetchMapData({ payload });
    },
    changeYear(direction) {
      let year = 1854;
      if (direction === 'increaseYear') {
        year = Number(this.mapYear) + 1;
      } else {
        year = Number(this.mapYear) - 1;
      }
      year = year.toString();
      const payload = {
        year,
      };
      this.fetchMapData({ payload });
    },
    update(close) {
      this.showModal = close;
      this.resetDrillDownData();
    },
    close(close) {
      this.showSentimentDrillDown = close;
    },
  },
};
</script>

<style lang="css" module>
.year-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.map-title {
  font-weight: bolder;
  font-size: 2em;
  text-transform: uppercase;
}

.selected-year {
  font-weight: bolder;
}

.single-year-change {
  display: flex;
  flex-direction: row;
  margin: 7px 0 7px 0;
}

.spacing-fix {
  margin: 0 10px 0 10px;
}

.subtitle-fix {
  margin: 7px 0 7px 0;
  text-align: center;
}

</style>