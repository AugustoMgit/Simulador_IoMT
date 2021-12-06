<template>
  <div>
    <b-navbar type="dark" variant="dark">

      <b-navbar-brand size="lg" to="/">
        <span class="main-icon">
          <strong>IoMT</strong>
        </span>
      </b-navbar-brand>

      <b-navbar-nav>
          <b-nav-item class="mr-3" to="/">Home</b-nav-item>
          <b-nav-item class="mr-3" to="/users">Users</b-nav-item>
          <b-nav-item class="mr-3" to="/dados-coletados">Dados Coletados</b-nav-item>
          <b-nav-item class="mr-3" to="/simulador">Simulador</b-nav-item>
      </b-navbar-nav>

      <b-nav-form class="ml-auto">
          <b-form-input size="sm" placeholder="Search"></b-form-input>
          <b-button size="sm" ><b-icon icon="search"></b-icon></b-button>
      </b-nav-form>

    </b-navbar>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.main-icon {
  font-family: serif;
}
</style>