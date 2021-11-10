<template>
  <div>
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from '@/components/generic/Navbar.vue';
import Footer from '@/components/generic/Footer.vue';

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
.center {
  text-align: center;
}

.title-size {
  font-size: 3em;
}

.font {
  font-family: 'Barlow', sans-serif;
}
</style>
