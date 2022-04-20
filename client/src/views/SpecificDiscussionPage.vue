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
          <div  v-for="point in graph_discussion_points" :key="point[0]">
            <h6>{{ point[1] }} Said:</h6>
            <p>
              {{ point[2] }}
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
    ...mapGetters('discussion', ['graph_discussion_points']),
  },
  methods: {
    ...mapActions(['common/login']),
    submitDiscussion(evt) {
      let userId = evt.target[0]._value;
      const payload = {
        userid: userId,
        message: this.message,
      };
      // this.$store.dispatch('common/login', { payload });
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
</style>