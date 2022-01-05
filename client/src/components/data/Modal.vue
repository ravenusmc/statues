<template>
  <div>
    <section id="clickaway" v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="font center modal-container">
            <!-- <h1>{{ modalTitle }}</h1> -->

            <!-- Modal Body area -->
            <!-- <div>
              <GChart
                :type="Table"
                :data="drillDownData"
                :options="chartOptionsDrillDown"
                :events="chartEvents"
                ref="gChart"
              />
            </div> -->
            <!-- End Modal Body area -->

            <!-- Modal Footer area -->
            <div class="modal-footer">
              <slot name="footer">
                <button class="font modal-default-button" @click="closeModal()">
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
export default {
	name: 'Modal',
	props: ['showModal'],
	methods: {
    closeModal() {
			console.log('hello');
      let modalClose = this.showModal;
      modalClose = false
      // this.$emit("update-number", modalClose);
    },
	}
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