<template>
  <div>
    <section :class="$style['discussion-section']">
      <div>
        <h1 :class="$style['user-heading']">
          Welcome
          <span :class="$style['name-fix']">{{ userObject.username }}</span
          >, tell us what you think!
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
              placeholder="What are your thoughts on this graph..."
            ></textarea>
          </div>
          <button class="button is-success">Submit</button>
        </form>
      </div>
      <div :class="$style['main-discussion-div']">
        <h1 :class="$style['user-heading']">What others have posted:</h1>
        <div>
          <div
            :class="$style['discussion-div']"
            v-for="point in graph_discussion_points"
            :key="point[0]"
          >
            <h6 :class="$style['name-div']">{{ point[1] }} Said:</h6>
            <p>
              {{ point[3] }}
            </p>
            <p>Discussion Sentiment: {{ point[4] }}</p>
            <form
              @submit.prevent="deleteDiscussion"
              v-if="point[0] == userObject.id"
            >
              <div>
                <input :value="point[2]" hidden />
                <input :value="selectedGraph" hidden />
              </div>
              <button class="button is-success font">Delete</button>
            </form>
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
    deleteDiscussion(evt) {
      let selectedDiscussion = evt.target[0]._value;
      let selectedGraph = evt.target[1]._value;
      const payload = {
        discussion_id: selectedDiscussion,
        graph_number: selectedGraph,
      }
      this.$store.dispatch('discussion/deleteDisscusionPost', { payload });
    }
  },
};
</script>

<style lang="css" module>
.discussion-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 500px;
  margin: 50px 50px 25px 50px;
}

.user-heading {
  font-size: 1.5em;
  text-align: center;
}

.name-fix {
  text-transform: capitalize;
}

.discussion-form {
  display: flex;
  align-items: center;
  justify-content: center;
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

.main-discussion-div {
  border-left: 3px solid black;
}

.discussion-div {
  margin: 15px 15px 15px 15px;
}
</style>