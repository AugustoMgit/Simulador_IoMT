<template>
  <div>
    <TopBar />
    <Content />
    <Footer />
  </div>
</template>

<script>
import TopBar from '@/components/layout/TopBar.vue'
import Content from '@/components/layout/Content.vue'
import Footer from '@/components/layout/Footer.vue'

export default {
  name: 'MainPage',
  components: { TopBar, Content, Footer },

}
</script>

<style>

</style>