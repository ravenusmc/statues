<template>
  <div>
    <div class="year-selection-area">
      <div class="input-area">
        <label class="fix-label-alignment" for="yearOne"
          >Enter First Year (1854-2017):</label
        >
        <input
          type="number"
          id="year"
          v-model="value.yearOne"
          name="yearOne"
          min="1854"
          max="2017"
          placeholder="1854"
        />
      </div>
      <div>
        <label for="yearTwo">Enter Second Year (1854-2017):</label>
        <input
          type="number"
          id="year"
          v-model="value.yearTwo"
          name="yearTwo"
          min="1854"
          max="2017"
          placeholder="2017"
        />
      </div>
    </div>
    <button class="button is-success font">Submit</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Years',
  props: {
    value: {
      type: Object,
      required: true,
    },
  },
  // data() {
  //   return {
  //     yearOne: 1854,
  //     yearTwo: 1900,
  //   };
  // },
  watch: {
    value() {
      this.$emit('input', this.value);
    },
  },
  methods: {},
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