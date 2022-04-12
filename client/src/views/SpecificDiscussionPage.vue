<template>
  <div>
    <h1>Welcome {{ userObject.username }} Tell us what you think!</h1>
    <section class='discussion_section'>
      <div>
        <form @submit.prevent="submitDiscussion">
          <div class="field">
            <input :value="userObject.id" hidden />
          </div>
          <div class="field">
            <textarea
              v-model="message"
              placeholder="What do you think..."
            ></textarea>
          </div>
          <button class="button is-success">Submit</button>
        </form>
      </div>
      <div>
        <h1>What others have posted:</h1>
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