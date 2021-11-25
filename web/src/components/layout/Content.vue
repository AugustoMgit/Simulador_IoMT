<template>
  <div class="main-content">
    <router-view />
  </div>
</template>

<script>
export default {
    name: 'Content'
}
</script>

<style>
.main-content {
  margin: 10px auto;
  width: 90%;
  min-width: 700px;
  min-height: 500px;
}
</style>