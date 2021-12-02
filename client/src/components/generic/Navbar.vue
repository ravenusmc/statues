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
              <router-link
                v-if="!loginFlag"
                class="fontColor font fix"
                to="/sign_up"
              >
                <a class="button is-primary">
                  <strong>Sign up</strong>
                </a>
              </router-link>
              <router-link
                v-if="!loginFlag"
                class="fontColor font fix"
                to="/login"
              >
                <a class="button is-light"> Login </a>
              </router-link>
              <router-link
                v-if="loginFlag"
                @click.native="logout"
                class="fontColor font"
                to="/login"
              >
                <a class="button is-light"> Log out </a>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'navbar',
  computed: {
    ...mapGetters('common', ['loginFlag']),
  },
  methods: {
    ...mapActions(['common/logout']),
    logout: function () {
      this.$store.dispatch('common/logout');
    },
  },
};
</script>

<style scoped>
.fix {
  margin-right: 10px;
}

.fontColor {
  color: white;
  font-weight: bolder;
  text-transform: uppercase;
}
</style>
