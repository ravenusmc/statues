<template>
  <div>
    <section :class="$style['discussion-section']">
      <div>
        <h1 class="center">
          Welcome {{ userObject.username }} Tell us what you think!
        </h1>
        <form
          :class="$style['discussion-form']"
          @submit.prevent="submitDiscussion"
        >
          <div>
            <input :value="userObject.id" hidden />
          </div>
          <div>
            <input :value="selectedGraph" hidden />
          </div>
          <div>
            <textarea
              rows="10"
              cols="55"
              v-model="message"
              placeholder="What do you think..."
            ></textarea>
          </div>
          <button class="button is-success">Submit</button>
        </form>
      </div>
      <div>
        <h1 class="center">What others have posted:</h1>
        <div>
          <div
            :class="$style['discussion-div']"
            v-for="point in graph_discussion_points"
            :key="point[0]"
          >
            <h6 :class="$style['name-div']">{{ point[1] }} Said:</h6>
            <p>
              {{ point[2] }}
            </p>
            <p>
              Discussion Sentiment: {{ point[3] }}
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'SpecificDiscussionPage',
  data() {
    return {
      message: '',
    };
  },
  computed: {
    ...mapGetters('session', ['userObject']),
    ...mapGetters('discussion', ['selectedGraph', 'graph_discussion_points']),
  },
  methods: {
    ...mapActions(['discussion/addDisscusionPost']),
    submitDiscussion(evt) {
      let userId = evt.target[0]._value;
      let selectedGraph = evt.target[1]._value;
      const payload = {
        userid: userId,
        graph_number: selectedGraph,
        post: this.message,
      };
      this.$store.dispatch('discussion/addDisscusionPost', { payload });
    },
  },
};
</script>

<style lang="css" module>
.discussion-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 500px;
  margin: 25px 50px 25px 50px;
}

.discussion-form {
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 3px solid black;
  min-height: 500px;
}

button {
  margin-left: 30px;
  margin-right: 15px;
}

.name-div {
  font-weight: bold;
  font-size: 1em;
  text-transform: uppercase;
}

.discussion-div {
  margin: 15px 15px 15px 15px;
}
</style>