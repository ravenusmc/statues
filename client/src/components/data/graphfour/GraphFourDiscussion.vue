<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Fourth Graph Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
      First, this graph does not allow the user to change the dates. It's 
      a graph that shows the top five states that removed statues after 
      Charlottesville. What is surprising to me is that the data shows that 
      the main state that removed statues was Texas. I did not expect this. 
      I actually thought that Georgia would have the most removed or maybe 
      North Carolina. Texas just seemes way to conservative for me. It really 
      makes me wonder why did Texas decide to pull so many statues down? Was 
      it done on the local or state levels or was it mass protest? 
    </p>
    <br />
    <p>
      
    </p>
  </div>
</template>

<script>
export default {
  name: 'GraphOneDiscussion',
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