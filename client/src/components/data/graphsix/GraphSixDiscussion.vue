<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Graph Six Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
    </p>
    <br />
    <p>

    </p>
  </div>
</template>

<script>
export default {
  name: 'GraphSixDiscussion',
};
</script>

<style scoped>
.responsive-phrase-large {
  display: block;
}

.responsive-phrase-small {
  display: none;
}

.graph-discussion {
  margin: 0 10% 0 10%;
}

.heading-title {
  font-weight: bolder;
  font-size: 2em;
  text-transform: uppercase;
  margin-bottom: 15px;
}

/* Responsive media quries */
@media only all and (max-width: 999px) {
  .responsive-phrase-large {
    display: none;
  }

  .responsive-phrase-small {
    display: block;
  }
}
</style>