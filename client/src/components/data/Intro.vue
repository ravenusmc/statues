<template>
  <div>
    <section>
      <div>
        <h1 class="font center title_data_page">The Purpose</h1>
      </div>
      <div>
        <p>This is a project that I've thought about for a while now.</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Intro',
};
</script>

<style scoped>
section {
	display: grid;
	grid-template-columns: 1fr 1fr;
	margin-top: 50px;
}

.title_data_page {
	font-weight: bolder;
	font-size: 4em;
	text-transform: uppercase;
}
</style>