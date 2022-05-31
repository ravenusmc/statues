<template>
  <div>
    <section id="clickaway" v-if="showSentimentDrillDown">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="font center modal-container">
            <h1>{{ modalTitle }}</h1>
            <hr />
            <!-- Modal Body area -->
            <div>
              <h3>On {{ drillDownData[6] }} {{ drillDownData[1] }} said: </h3>
              <p>
                {{ drillDownData[3] }}
              </p>
              <h3>Sentiment: {{ drillDownData[4] }}</h3>
            </div>
            <!-- End Modal Body area -->
            <hr />
            <!-- Modal Footer area -->
            <div class="modal-footer">
              <slot name="footer">
                <button class="button is-success" @click="closeSentimentModal()">
                  Close
                </button>
              </slot>
            </div>
            <!-- End Modal Footer area -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Modal',
  props: ['showSentimentDrillDown', 'modalTitle'],
  computed: {
    ...mapGetters('data', ['drillDownData']),
  }, // End Computed Area
  methods: {
    closeSentimentModal() {
      let closeSentimentModal = this.showSentimentDrillDown;
      closeSentimentModal = false;
      this.$emit('close-sentiment-modal', closeSentimentModal);
    },
  },
};

</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  width: 600px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
.modal-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
</style>