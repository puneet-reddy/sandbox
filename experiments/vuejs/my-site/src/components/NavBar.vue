<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">{{title}}</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/" href="#">Home</b-nav-item>
          <b-nav-item href="#" disabled>Blogs</b-nav-item>
          <b-nav-item href="#" disabled>Code</b-nav-item>
          <b-nav-item href="#" disabled>Rants</b-nav-item>
          <b-nav-item href="#" disabled>Analyses</b-nav-item>
          <b-nav-item to="/about" href="#">About</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <!-- removing the search till I can get it working the way I want -->
          <!-- <b-nav-form>
            <b-form-input disabled size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button disabled size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right disabled>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    title: String
  }
}
</script>
