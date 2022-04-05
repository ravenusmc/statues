<template>
  <div>
    <section>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph One</h6>
        <p>This graph shows Statues in North Vs South</p>
      </div>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph Two</h6>
        <p>This graph shows the states with the most statues</p>
      </div>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph Three</h6>
        <p>This graph shows Statues by state</p>
      </div>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph Four</h6>
        <p>This graph shows Top 5 states that removed statues</p>
      </div>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph Five</h6>
        <p>This graph shows the last ten years of statue removal</p>
      </div>
      <div class="graph_discussion_div">
        <h6 class="discussion_title">Discuss Graph Six</h6>
        <p>This graph shows Statue type by state and time period
</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Discussion',
};
</script>

<style lang="css" scoped>
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-top: 100px;
  margin-bottom: 100px;
  align-items: center;
  justify-items: center;
}

.graph_discussion_div {
  border: 2px solid black;
  text-align: center;
  width: 50%;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 25px;
}

.discussion_title {
  font-weight: bold;
}
</style>