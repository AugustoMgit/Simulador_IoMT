<template>
  <div class="footer text-center p-3">
    <span>© 2021 Sistemas Distribuídos <a href="https://www.upf.br/">UPF</a></span>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>

.footer {
  position: fixed;
  flex-flow: row nowrap;
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #343a40;
  color: rgb(255, 255, 255, .5);
}

</style>