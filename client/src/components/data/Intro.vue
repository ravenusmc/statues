<template>
  <div>
    <section>
      <div class="title-div">
        <h1 class="font center title-data-page">The Purpose</h1>
      </div>
      <div class='paragraph-div'>
        <p>
          This is a project that I've thought about for a while now. I'd say
          that it goes back at least four years. For some reason I kept putting
          it off - even though it was a project that really interested me. Then,
          one day, about a year ago, I found some good data on Confederate
          Statues. I knew that I had to get going on this project to build it -
          the data was the main thing holding me back.
        </p>
        <br />
        <p>
          The main purpose of this project is to look at Confederate Statue data
          so that the user can see when did the most statues go up. I believe
          that this will be between 1890 - 1930. I'm someone that believes that
          Confederate statues do belong in a museum. What the Confederacy stood
          for was wrong. I do have visions that I could use this project to
          inform friends and family about the statues. Maybe, if I'm lucky, I
          can change some opinions.
        </p>
        <br />
        <p>
          Finally, I was browsing Reddit, specifically the section on Ask
          Reddit. Some one asked the question: What do you think of the
          Confederate flag. The first answer was by a guy who said he grew up in
          the South and was taught to worship the culture. As he got older he
          educated himself more about the Civil War. He came to the conclusion
          that Confederate memorbia is wrong. He ended with this line: "A flag
          against oppression shouldn't leave people of color feeling oppressed".
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
  grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
  margin: 50px 0 50px 0;
}

.title-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title-data-page {
  font-weight: bolder;
  font-size: 4em;
  text-transform: uppercase;
}

/****************
Media Queries
****************/

/* Mobile Screen */
@media only all and (max-width: 900px) {

	.title-div {
		margin-bottom: 25px;
	}

 .paragraph-div {
	 margin: 0 5% 0 5%;
 }

}
</style>