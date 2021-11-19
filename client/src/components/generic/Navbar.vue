<template>
  <div>
    <nav
      class="navbar is-danger"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">
        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            <router-link class="fontColor font" to="/">Home</router-link>
          </a>
          <a class="navbar-item">
            <router-link class="fontColor font" to="/about">About</router-link>
          </a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link class="fontColor font" to="/sign_up">
                <a class="button is-primary">
                  <strong>Sign up</strong>
                </a>
              </router-link>
              <router-link class="fontColor font" to="/login">
                <a class="button is-light"> Log in </a>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'navbar',
};
</script>

<style scoped>
</style>
