<template>
  <div>
    <Modal
      :data="drillDownDataGraphOne"
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
    ...mapGetters('data', ['graphOneYearOne', 'graphOneYearTwo', 'drillDownDataGraphOne']),
  },
  data() {
    return {
      modalTitle: '',
      showModal: false,
      chartEvents: {
        select: () => {
          // console.log(this.data); // This will show you the data kept for reference
          const chart = this.$refs.gChart.chartObject;
          const selection = chart.getSelection()[0];
          let row = selection.row + 1;
          let side = this.data[row][0];
          this.showModal = true;
          let graphOneYearOne = this.graphOneYearOne;
          let graphOneYearTwo = this.graphOneYearTwo;
          const payload = {
            graphOneYearOne,
            graphOneYearTwo,
            side,
          };
          this.$store.dispatch('data/fetchDrillDownDataGraphOne', { payload });
          this.modalTitle = `Statues in the ${side} between ${graphOneYearOne} - ${graphOneYearTwo}`
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
