<template>
  <div>
    <form @submit="submitForm">
      <div class="year-selection-area">
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
    ...mapActions('data', ['fetchTopFiveByYear']),
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
        this.fetchTopFiveByYear({ payload });
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

</style>