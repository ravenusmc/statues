<template>
  <div>
    <h1>Welcome {{ userObject.username }}</h1>
			<section>
	</section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'SpecificDiscussionPage',
  computed: {
    ...mapGetters('session', ['userObject']),
  },
};
</script>