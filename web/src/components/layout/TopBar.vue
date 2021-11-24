<template>
  <div>
    <b-navbar type="dark" variant="dark">

        <b-navbar-nav>
            <b-nav-item class="ml-4" to="/">Home</b-nav-item>
            <b-nav-item class="ml-4" to="/register-user">New User</b-nav-item>
            <b-nav-item class="ml-4" to="#">Statistics</b-nav-item>
        </b-navbar-nav>

        <b-nav-form class="ml-auto">
            <b-form-input placeholder="Search"></b-form-input>
            <b-button><b-icon icon="search"></b-icon></b-button>
        </b-nav-form>

    </b-navbar>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>