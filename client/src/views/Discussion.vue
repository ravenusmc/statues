<template>
  <div>
    <h1 :class="$style['discussion-title']">
      Please Select a Graph to Discuss
    </h1>
    <section :class="$style['discussion-section']">
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph One</h6>
          <p>This graph shows Statues in North Vs South</p>
          <input :value="1" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph Two</h6>
          <p>This graph shows the states with the most statues</p>
          <input :value="2" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph Three</h6>
          <p>This graph shows Statues by state</p>
          <input :value="3" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph Four</h6>
          <p>This graph shows Top 5 states that removed statues</p>
          <input :value="4" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph Five</h6>
          <p>This graph shows the last ten years of statue removal</p>
          <input :value="5" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
      <div :class="$style['graph_discussion_div']">
        <form @submit.prevent="selectedGraphForDiscussion">
          <h6 :class="$style['discussion_title']">Discuss Graph Six</h6>
          <p>This graph shows Statue type by state and time period</p>
          <input :value="6" hidden />
          <button type="submit" class="btn btn-outline-dark">Discuss</button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Discussion',
  methods: {
    ...mapActions(['discussion/getDisscusionData']),
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

<style lang="css" module>
.discussion-title {
  text-align: center;
  font-weight: bolder;
  font-size: 32px;
  margin-top: 50px;
}

.discussion-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-top: 20px;
  margin-bottom: 100px;
  align-items: center;
  justify-items: center;
}

.graph_discussion_div {
  border: 2px solid black;
  text-align: center;
  width: 50%;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 25px;
  border-radius: 15px;
}

.discussion_title {
  font-weight: bold;
}
</style>