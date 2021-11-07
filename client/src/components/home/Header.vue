<template>
  <div>
    <section>
			<div class='title-div'>
				<h1>Confederate Statues</h1>
			</div>
		</section>
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

section {
	height: 100vh;
	background-image: url("../../assets/images/lone_Statue.jpg");
	background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
	margin-bottom: 25px;
}

.title-div {
	position: absolute;
	margin-left: 10%;
	top: 200px;
}

h1 {
	font-weight: bold;
	text-transform: uppercase;
	font-size: 3em;
}
</style>