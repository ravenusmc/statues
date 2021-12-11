<template>
	<div>
		<h1 class='center font'>Discussion</h1>
		<p>
			<span class='responsive-phrase-large'>The graph to the right...</span><span class='responsive-phrase-small'>The below graph...</span>
		</p>
	</div>
</template>

<script>
export default {
	name: 'GraphOneDiscussion',
}
</script>

<style scoped>

.responsive-phrase-small {
	display: none;
}

/* Responsive media quries */
@media only all and (max-width: 768px) {
	.responsive-phrase-large {
		display: none
	}

	.responsive-phrase-small {
		display: block;
	}
}

</style>