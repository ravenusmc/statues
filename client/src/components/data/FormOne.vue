<template>
  <div>
    <form @submit="submitForm">
      <div class="year-selection-area">
        <label for="yearOne">Enter First Year (1870-1950):</label>
        <input
          type="number"
          id="year"
          v-model="yearOne"
          name="yearOne"
          min="1870"
          max="1950"
        />
        <label for="yearTwo">Enter Second Year (1870-1950):</label>
        <input
          type="number"
          id="year"
          v-model="yearTwo"
          name="yearTwo"
          min="1870"
          max="1950"
        />
      </div>
      <button class="button is-success font">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'FormOne',
  data() {
    return {
      yearOne: 1870,
      yearTwo: 1870,
    };
  },
  methods: {
    submitForm(evt) {
      evt.preventDefault();
      console.log(this.yearOne);
      console.log(this.yearTwo);
      // this.startDate = moment(this.startDate).format('M/D/YYYY h:mm:ss A');
      // this.endDate = moment(this.endDate).format('M/D/YYYY h:mm:ss A');
      const payload = {
        yearOne: this.yearOne,
        yearTwo: this.yearTwo,
      };
      // this.fireActions({ payload });
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

button {
  margin: 15px 0 15px 0;
}

.year-selection-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>