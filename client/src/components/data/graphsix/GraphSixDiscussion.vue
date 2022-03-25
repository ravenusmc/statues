<template>
  <div class="graph-discussion">
    <h1 class="center font heading-title">Graph Six Discussion</h1>
    <p>
      <span class="responsive-phrase-large">The graph to the right...</span>
      <span class="responsive-phrase-small">The below graph...</span>
    </p>
    <br />
    <p>
      I don't believe there's anything super interesting on this graph - like how 
      a lot of the other drive home the point that there's a lot more statues in the South then 
      there are in the North. What this graph does show is that it appears that the most common way
      to honor the dead is through monuments. This makes sense. I think that throughout history 
      this would be the most common way to honor those who fought. People want to be seen in granite 
      or marble - to truly last through the ages. After that comes the roads and schools being named - even 
      the name of a county. That monumnet though is going to last a long time and really show people how 
      important something is when you make a large statue of it. 
    </p>
    <br />
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