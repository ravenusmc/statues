<template>
  <div>
    <section>
      <div>
        <h1 class="font center title_data_page">The Purpose</h1>
      </div>
      <div>
        <p>
					This is a project that I've thought about for a while now. I'd say that it goes back 
					at least four years. For some reason I kept putting it off - even though it was a project 
					that really interested me. Then, one day, about a year ago, I found some good data on 
					Confederate Statues. I knew that I had to get going on this project to build it - the data 
					was the main thing holding me back. 
				</p>
				<br>
				<p>
					The main purpose of this project is to look at Confederate Statue data so that the 
					user can see when did the most statues go up. I believe that this will be between 
					1890 - 1930. 
				</p>
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