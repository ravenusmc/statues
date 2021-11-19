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
}
</style>
