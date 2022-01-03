<template>
  <div class='graph-discussion'>
    <h1 class="center font">Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
      There's one thing that stands out to me on the graph. The South always appears 
      to have more statues than the North. The North won the war. I almost would have thought 
      that the North would have had more statues up until about 1890. That is very clearly 
      not the case. From the start, according to the data, the South had way more statues than 
      the North did.
    </p>
  </div>
</template>

<script>
export default {
  name: 'GraphOneDiscussion',
};
</script>

<style scoped>
.responsive-phrase-small {
  display: none;
}

.graph-discussion {
  margin: 0 10% 0 10%;
}

/* Responsive media quries */
@media only all and (max-width: 768px) {
  .responsive-phrase-large {
    display: none;
  }

  .responsive-phrase-small {
    display: block;
  }
}
</style>