<template>
  <div class="content">
    <div class="content-left">
      <p><router-link to="/body/trianglearea">area of triangle</router-link></p>
      <p><router-link to="/body/maxedge">max edge</router-link></p>
      <p><router-link to="/body/conversion">conversion</router-link></p>
      <p><router-link to="/body/recurse">recursion</router-link></p>
    </div>
    <div id="content-right">
      <router-view></router-view>
    </div>
  </div>
</template>
<style scoped>
.content {
  height: 100%;
}
.content-left {
  width: 20%;
  height: 700px;
  float: left;
  background: transparent;
  text-align: center;
}
.content-left a {
  color: black;
}
#content-right {
  width: 80%;
  height: 700px;
  float: right;
  background-color: black;
}
</style>
