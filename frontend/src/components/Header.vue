<template>
  <div class="header">
    <div class="header-logo">
      <router-link to="/">Dokimi</router-link>
    </div>
    <div class="header-element">
      <router-link to="/body/bodygreeting">dashboard</router-link>
    </div>
    <div class="header-element">
      <router-link to="/faq">FAQ</router-link>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.header {
  width: 100%;
  z-index: 10;
  height: 90px;
  position: absolute;
  top: 0;
  margin-top: 0.2em;
  background-color: #33ff33;
}
.header-logo {
  margin: 20px;
  float: left;
  font-weight: 900;
  font-size: 2.5em;
}
.header-logo a {
  color: black;
}
.header-element {
  margin: 30px;
  float: right;
}
.header-element a {
  color: black;
}
</style>
