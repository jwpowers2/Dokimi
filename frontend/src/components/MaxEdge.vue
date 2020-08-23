<template>
  <div class="maxedge">
    <h1>Max Edge</h1>
    <div class="message">{{ message }}</div>
    <form>
      <input v-model="intOne" placeholder="side one" />
      <input v-model="intTwo" placeholder="side two" />
      <input type="button" @click="submitNumbers" value="Submit" />
    </form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      intOne: null,
      intTwo: null,
      message:
        "Enter the length of two sides of a triangle \
      to find the maximum size of the other edge."
    };
  },
  methods: {
    submitNumbers() {
      if (this.intOne !== null && this.intTwo !== null) {
        let one = parseInt(this.intOne);
        let two = parseInt(this.intTwo);
        if (typeof one === "number" && typeof two === "number") {
          let data = { intOne: one, intTwo: two };
          axios.post("http://127.0.0.1:5000/api/maxedge", data).then(
            response => {
              this.message = "thank you for your submission";
              this.intOne = null;
              this.intTwo = null;
              this.message = `The maximum size for the other side of the triangle is: ${response.data}`;
            },
            error => {
              this.message = error;
            }
          );
        } else {
          this.message = "you must enter an integer for each field";
        }
      } else {
        this.message = "you must enter an integer for both sides";
      }
    }
  }
};
</script>
<style>
.maxedge {
  text-align: center;
  width: 100%;
  height: 100%;
  color: #33ff33;
}
.maxedge input {
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
