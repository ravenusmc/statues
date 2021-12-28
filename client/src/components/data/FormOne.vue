<template>
  <div>
    <form @submit="submitForm">
      <div class="year-selection-area">
        <div class='input-area'>
          <label for="yearOne">Enter First Year (1854-2017):</label>
          <input
            type="number"
            id="year"
            v-model="yearOne"
            name="yearOne"
            min="1854"
            max="2017"
          />
        </div>
        <div>
          <label for="yearTwo">Enter Second Year (1854-2017):</label>
          <input
            type="number"
            id="year"
            v-model="yearTwo"
            name="yearTwo"
            min="1854"
            max="2017"
          />
        </div>
      </div>
      <button class="button is-success font">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'FormOne',
  data() {
    return {
      yearOne: 1854,
      yearTwo: 2017,
    };
  },
  methods: {
    ...mapActions('data', ['fetchNorthSouthByYear']),
    submitForm(evt) {
      evt.preventDefault();
      // this.startDate = moment(this.startDate).format('M/D/YYYY h:mm:ss A');
      // this.endDate = moment(this.endDate).format('M/D/YYYY h:mm:ss A');
      const payload = {
        yearOne: this.yearOne.toString(),
        yearTwo: this.yearTwo.toString(),
      };
      this.fetchNorthSouthByYear({ payload });
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

.input-area {
  display: flex;
  flex-direction: row;
}
</style>