<template>
  <div>
    <form @submit="submitForm">
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
    <form @submit.prevent="selectedGraphForDiscussion">
      <h6>Discuss Graph One</h6>
      <input :value="1" hidden />
      <button type="submit" class="btn btn-outline-dark">
        Go to Discussion
      </button>
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
    ...mapActions(['discussion/getDisscusionData']),
    submitForm(evt) {
      evt.preventDefault();
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
          yearOne,
          yearTwo,
        };
        this.fetchNorthSouthByYear({ payload });
      }
    },
    selectedGraphForDiscussion(evt) {
      let selectedValue = evt.target[0]._value;
      const payload = {
        selectedGraphDiscussion: selectedValue,
      };
      this.$store.dispatch('discussion/getDisscusionData', { payload });
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