<template>
  <div>
    <section>
      <div class="graph_discussion_div">
        <h6>Discuss Graph One</h6>
      </div>
      <div class="graph_discussion_div">
        <h6>Discuss Graph Two</h6>
      </div>
      <div class="graph_discussion_div">
        <h6>Discuss Graph Three</h6>
      </div>
      <div class="graph_discussion_div">
        <h6>Discuss Graph Four</h6>
      </div>
      <div class="graph_discussion_div">
        <h6>Discuss Graph Five</h6>
      </div>
      <div class="graph_discussion_div">
        <h6>Discuss Graph Six</h6>
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
  border: 2px solid red;
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
</style>