<template>
  <div>
    <form @submit="submitForm">
      <div>
        <label for="year">Select Year (10-100):</label>
        <input
          type="number"
          id="year"
					v-model="year"
          name="year"
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
      year: 1870,
    };
  },
  methods: {
    submitForm(evt) {
			evt.preventDefault();
			console.log(this.year);
      // this.startDate = moment(this.startDate).format('M/D/YYYY h:mm:ss A');
      // this.endDate = moment(this.endDate).format('M/D/YYYY h:mm:ss A');
      // const payload = {
      //   category: this.category,
      //   state: this.state,
      //   currency: 'USD',
      //   country: 'US',
      //   startDate: this.startDate,
      //   endDate: this.endDate,
      //   moneyGoal: this.moneyGoal,
      //   backers: this.backers,
      // };
      // this.fireActions({ payload });
    },
  },
};
</script>