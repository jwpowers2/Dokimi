<template>
  <div class="trianglearea">
    <h1>triangle area</h1>
    <div class="message">{{ message }}</div>
    <form>
      <input v-model="sideOne" placeholder="side one" />
      <input v-model="sideTwo" placeholder="side two" />
      <input v-model="sideThree" placeholder="side three" />
      <input
        v-model="angleOfIntersection"
        placeholder="angle of Intersection"
      />
      <input type="button" @click="submitSides" value="Submit" />
    </form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      message:
        "provide the length of all three sides\
      or provide the length of two sides (side one and side two) and the angle\
      where they intersect",
      sideOne: null,
      sideTwo: null,
      sideThree: null,
      angleOfIntersection: null
    };
  },
  methods: {
    submitSides() {
      if (this.sideOne !== null && this.sideTwo !== null) {
        let sideOne = parseInt(this.sideOne);
        let sideTwo = parseInt(this.sideTwo);
        if (this.sideThree === null && this.angleOfIntersection === null) {
          this.message =
            "if side three is not included, you must enter an angle of intersection";
          return;
        } else {
          let sideThree = parseInt(this.sideThree);
          let angleOfIntersection = parseInt(this.angleOfIntersection);
          let data = {
            sideOne: sideOne,
            sideTwo: sideTwo,
            sideThree: sideThree,
            angleOfIntersection: angleOfIntersection
          };
          axios.post("http://127.0.0.1:5000/api/area", data).then(
            response => {
              this.sideOne = null;
              this.sideTwo = null;
              this.sideThree = null;
              this.angleOfIntersection = null;
              this.message = `The area of the triangle is: ${response.data}`;
            },
            error => {
              this.message = error;
            }
          );
        }
      } else {
        this.message = "you must enter the length of at least two sides";
      }
    }
  }
};
</script>
<style scoped>
.trianglearea {
  text-align: center;
  color: #33ff33;
  width: 100%;
  height: 100%;
}
.trianglearea input {
  margin-right: 10px;
  font-size: 1em;
  border-radius: 5px;
}
.message {
  width: 50%;
  height: 30%;
  margin: 0 auto;
}
</style>
