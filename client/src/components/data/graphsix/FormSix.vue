<template>
  <div>
    <form @submit="submitForm">
      <select v-model="state">
        <option>Please select a State</option>
        <option v-for="state in states" :key="state">{{ state }}</option>
      </select>
      <div class="year-selection-area">
        <div class="input-area">
          <label class="fix-label-alignment" for="yearOne"
            >Enter First Year (1854-2017):</label
          >
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
  name: 'FormSix',
  data() {
    return {
      state: 'AK',
      states: [
        'AK',
        'AL',
        'AR',
        'AZ',
        'CA',
        'DC',
        'DE',
        'FL',
        'GA',
        'IA',
        'IN',
        'KS',
        'KY',
        'MA',
        'MD',
        'ME',
        'MS',
        'MT',
        'NC',
        'NM',
        'NV',
        'NY',
        'OH',
        'OKPAMOLAID',
        'OR',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VA',
        'WA',
        'WV',
      ],
      yearOne: 1854,
      yearTwo: 2017,
    };
  },
  methods: {
    ...mapActions('data', ['fetchNorthSouthByYear']),
    submitForm(evt) {
      evt.preventDefault();
      let state = this.state;
      let yearOne = Number(this.yearOne);
      let yearTwo = Number(this.yearTwo);
      if (yearOne >= yearTwo) {
        alert('Year One must be less than year two.');
      } else if (yearTwo <= yearOne) {
        alert('Year Two must be greater than year one');
      } else if (yearOne === yearTwo) {
        alert('The years cannot be the same.');
      } else {
        const payload = {
          state,
          yearOne,
          yearTwo,
        };
        this.fetchNorthSouthByYear({ payload });
      }
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
  margin-bottom: 5px;
}

.fix-label-alignment {
  margin-left: -23px;
}
</style>