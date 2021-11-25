<template>
  <div class="main-page">
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
.main-page {
  background-color: rgba(255, 255, 255, 0.418);
}
</style>