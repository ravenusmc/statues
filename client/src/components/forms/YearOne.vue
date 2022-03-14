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
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'YearOne',
  data() {
    return {
      yearOne: 1854,
    };
  },
  methods: {

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