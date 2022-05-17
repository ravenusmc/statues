<template>
  <div>
    <section :class="$style['discussion-section']" v-if="showDiscussion">
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
        <section :class="$style['page-options']">
          <div :class="$style['selection-div']">
            <select @change="onChange($event)" v-model="order">
              <option>Please select an ordering option</option>
              <option v-for="order in ordering_options" :key="order">
                {{ order }}
              </option>
            </select>
          </div>
          <div :class="$style['selection-div']">
            <select @change="changeDisplay($event)" v-model="view">
              <option>Select Discussion or Graph</option>
              <option v-for="view in views" :key="view">
                {{ view }}
              </option>
            </select>
          </div>
        </section>
        <div>
          <div
            :class="$style['discussion-div']"
            v-for="point in graph_discussion_points"
            :key="point[2]"
          >
            <h6 :class="$style['name-div']">{{ point[1] }} Said:</h6>
            <p>
              {{ point[3] }}
            </p>
            <p :class="$style['name-div']">Date Posted: {{ point[6] }}</p>
            <p :class="$style['name-div']">Votes: {{ point[5] }}</p>
            <svg
              @click="
                changeValueOfDiscussionPoint(
                  1,
                  point[2],
                  point[5],
                  selectedGraph
                )
              "
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              class="bi bi-arrow-up-square-fill"
              viewBox="0 0 16 16"
              :class="$style['spacing-fix']"
            >
              <path
                d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 1 0z"
              />
            </svg>
            <svg
              @click="
                changeValueOfDiscussionPoint(
                  -1,
                  point[2],
                  point[5],
                  selectedGraph
                )
              "
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              class="bi bi-arrow-down-square-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2zm6.5 4.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5a.5.5 0 0 1 1 0z"
              />
            </svg>
            <div :class="$style['sentiment-delete-div']">
              <p>Discussion Sentiment: {{ point[4] }}</p>
              <form
                @submit.prevent="deleteDiscussion"
                v-if="point[0] == userObject.id"
              >
                <div>
                  <input :value="point[2]" hidden />
                  <input :value="selectedGraph" hidden />
                </div>
                <button class="button is-danger font">Delete</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <!-- Place graph section here -->
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
      order: 'Newest',
      ordering_options: ['Newest', 'Oldest', 'Most Popular', 'Least Popular'],
      view: 'Discussion',
      views: ['Discussion', 'Graph of Discussion Sentiment'],
      showDiscussion: true,
    };
  },
  computed: {
    ...mapGetters('session', ['userObject']),
    ...mapGetters('discussion', ['selectedGraph', 'graph_discussion_points']),
  },
  methods: {
    ...mapActions('discussion', [
      'addDisscusionPost',
      'deleteDisscusionPost',
      'switchDiscussionOrdering',
      'changeDiscussionVotes',
    ]),
    submitDiscussion(evt) {
      let userId = evt.target[0]._value;
      let selectedGraph = evt.target[1]._value;
      const payload = {
        userid: userId,
        graph_number: selectedGraph,
        post: this.message,
      };
      this.addDisscusionPost({ payload });
      this.message = '';
    },
    deleteDiscussion(evt) {
      let selectedDiscussion = evt.target[0]._value;
      let selectedGraph = evt.target[1]._value;
      const payload = {
        discussion_id: selectedDiscussion,
        graph_number: selectedGraph,
      };
      this.deleteDisscusionPost({ payload });
    },
    onChange(event) {
      let ordering = event.target.value;
      let column = '';
      let direction = '';
      if (ordering === 'Newest') {
        column = 'created';
        direction = 'DESC';
      } else if (ordering === 'Oldest') {
        column = 'created';
        direction = 'ASC';
      } else if (ordering === 'Most Popular') {
        column = 'votes';
        direction = 'DESC';
      } else {
        column = 'votes';
        direction = 'ASC';
      }
      const payload = {
        column,
        direction,
        graph_number: this.selectedGraph,
      };
      this.switchDiscussionOrdering({ payload });
    },
    changeDisplay(event) {
      if (this.view == 'Graph of Discussion Sentiment') {
        this.showDiscussion = false
      }
    },
    changeValueOfDiscussionPoint(value, discussionID, votes, selectedGraph) {
      // I belive that this conditional statement will be able to be removed shortly
      // just have to fix a few things...
      if (votes === null) {
        votes = 0;
      }
      let numberOfVotesCalculated = votes + value;
      if (numberOfVotesCalculated < 0) {
        numberOfVotesCalculated = 0;
      }
      const payload = {
        discussionID,
        numberOfVotesCalculated,
        selectedGraph,
      };
      this.changeDiscussionVotes({ payload });
    },
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

.sentiment-delete-div {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 15px;
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

.page-options {
  display: flex; 
  flex-direction: row;
  justify-content: space-between;
  margin-left: 5px;
}

.discussion-div {
  margin: 15px 15px 15px 15px;
}

.spacing-fix {
  margin-right: 10px;
}
</style>