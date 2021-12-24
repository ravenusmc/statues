<template>
  <div>
    <form @submit="submitForm">
      <div>
        <label for="yearOne">Enter First Year (1870-):</label>
        <input
          type="number"
          id="year"
          v-model="yearOne"
          name="yearOne"
          min="1870"
          max="1950"
        />
        <label for="yearTwo">Enter Second Year (1870-100):</label>
        <input
          type="number"
          id="year"
          v-model="yearTwo"
          name="yearTwo"
          min="1870"
          max="1950"
        />
        <button class="font">Submit</button>
      </div>
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
			console.log(this.yearTwo)
      // this.startDate = moment(this.startDate).format('M/D/YYYY h:mm:ss A');
      // this.endDate = moment(this.endDate).format('M/D/YYYY h:mm:ss A');
      // const payload = {
      //   year: this.year,
      // };
      // this.fireActions({ payload });
    },
  },
};
</script>