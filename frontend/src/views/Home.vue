<template>
  <div>
    <Header />
    <h1 class="homeGreeting" v-if="isHome">
      <router-link to="/body/bodygreeting"
        >Enter Dokimi Dashboard Here</router-link
      >
      <br />or<br />
      <router-link to="/faq">See the FAQ for more info</router-link>
    </h1>
    <div class="assessmentbody"><router-view /></div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
export default {
  name: "Home",
  components: { Header },
  computed: {
    isHome() {
      if (this.$route.name === "Home") {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>
<style scoped>
.assessmentbody {
  margin-top: 100px;
}
.homeGreeting {
  margin-top: 300px;
  text-align: center;
}
.homeGreeting a {
  color: black;
}
</style>
