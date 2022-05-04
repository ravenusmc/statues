<template>
  <div>
    <section>
      <div class="image"></div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LoginPicture',
};
</script>

<style scoped>
.image {
  margin: 5% 5% 5% 5%;
  height: 80vh;
  width: auto;
  background-image: url('../../assets/images/login.jpg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  clip-path: polygon(20% 0, 80% 0, 100% 100%, 0 100%);
}

@media only all and (max-width: 900px) {
  section {
    margin: 1% 5% 5% 1%;
  }
}
</style>
