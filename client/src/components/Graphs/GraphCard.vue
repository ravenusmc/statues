<template>
  <div>
    <Modal
      :data="drillDownData"
      :showModal="showModal"
      :modalTitle="modalTitle"
      @close-modal="update"
    />
    <GChart
      :type="typeOne"
      :data="data"
      :options="options"
      :events="chartEvents"
      ref="gChart"
    />
  </div>
</template>

<script>
import Modal from '@/components/data/Modal.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'GraphCard',
  props: ['typeOne', 'data', 'options'],
  components: {
    Modal,
  },
  computed: {
    ...mapGetters('data', [
      'graphOneYearOne',
      'graphOneYearTwo',
      'drillDownData',
      'graphTwoYearOne',
      'graphTwoYearTwo',
      'graphThreeYearOne',
      'graphThreeYearTwo',
    ]),
  },
  data() {
    return {
      modalTitle: '',
      showModal: false,
      // Code in here could be cleaned up some more...
      chartEvents: {
        select: () => {
          //console.log(this.data); // This will show you the data kept for reference
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          if (this.data[0].length === 4) {
            let side_selected = this.data[0][selection.column];
            let graphThreeYearOne = this.graphThreeYearOne;
            let graphThreeYearTwo = this.graphThreeYearTwo;
            let state = this.data[1][0]
            const payload = {
              graphThreeYearOne,
              graphThreeYearTwo,
              state,
              side_selected,
            };
            this.$store.dispatch('data/fetchDrillDownDataGraphThree', {
              payload,
            });
            this.modalTitle = `Statues in the state of ${state} between ${graphThreeYearOne} - ${graphThreeYearTwo}
            that are for the ${side_selected}`;
          } else if (this.data[0][0] === 'Side') {
            let row = selection.row + 1;
            let side = this.data[row][0];
            let graphOneYearOne = this.graphOneYearOne;
            let graphOneYearTwo = this.graphOneYearTwo;
            const payload = {
              graphOneYearOne,
              graphOneYearTwo,
              side,
            };
            this.$store.dispatch('data/fetchDrillDownDataGraphOne', {
              payload,
            });
            this.modalTitle = `Statues in the ${side} between ${graphOneYearOne} - ${graphOneYearTwo}`;
          } else if (this.data[0][0] === 'State') {
            let row = selection.row + 1;
            let state = this.data[row][0];
            let graphTwoYearOne = this.graphTwoYearOne;
            let graphTwoYearTwo = this.graphTwoYearTwo;
            const payload = {
              graphTwoYearOne,
              graphTwoYearTwo,
              state,
            };
            this.$store.dispatch('data/fetchDrillDownDataGraphTwo', {
              payload,
            });
            this.modalTitle = `Statues in ${state} between ${graphTwoYearOne} - ${graphTwoYearTwo}`;
          }
          this.showModal = true;
        },
      }, // End Chart Events
    };
  }, // End of data
  methods: {
    update(close) {
      this.showModal = close;
    },
  }, // End of Methods
};
</script>
