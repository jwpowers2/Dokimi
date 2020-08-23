<template>
  <div class="recursion">
    <h1>recursion</h1>
    <div class="message">{{ message }}</div>
    <form>
      <input v-model="messageRe" placeholder="message" />
      <input v-model="countRe" placeholder="count" />
      <input type="button" @click="submitMessage" value="Submit" />
    </form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      messageRe: null,
      countRe: null,
      message:
        "Enter the message you want repeated using recursion \
      as well as the count for how many repetitions."
    };
  },
  methods: {
    submitMessage() {
      if (this.intOne !== null && this.intTwo !== null) {
        let count = parseInt(this.countRe);
        if (typeof count === "number" && typeof this.messageRe === "string") {
          let data = { message: this.messageRe, count: count };
          axios.post("http://127.0.0.1:5000/api/recursion", data).then(
            response => {
              this.messageRe = null;
              this.countRe = null;
              this.message = `the recursive response is: ${response.data}`;
            },
            error => {
              this.message = error;
            }
          );
        } else {
          this.message =
            "you must enter a string for message and an integer for count";
        }
      } else {
        this.message = "you must enter a value for both fields";
      }
    }
  }
};
</script>
<style scoped>
.recursion {
  text-align: center;
  width: 100%;
  height: 100%;
  color: #33ff33;
}
.recursion input {
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
