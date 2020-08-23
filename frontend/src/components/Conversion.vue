<template>
  <div class="conversion">
    <h1>conversion to seconds</h1>
    <div class="message">{{ message }}</div>
    <form>
      <input v-model="hours" placeholder="hours" />
      <input v-model="minutes" placeholder="minutes" />
      <input type="button" @click="submitSeconds" value="Submit" />
    </form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      message:
        "Convert hours and/or minutes into seconds.\
                Enter an integer for number of hours and/or minutes",
      minutes: null,
      hours: null
    };
  },
  methods: {
    submitSeconds() {
      if (this.minutes === null && this.hours === null) {
        this.message = "one input must be filled";
      } else {
        let minutes = parseInt(this.minutes);
        let hours = parseInt(this.hours);
        if (typeof minutes === "number" && typeof hours === "number") {
          let data = { minutes: minutes, hours: hours };
          axios.post("http://127.0.0.1:5000/api/seconds", data).then(
            response => {
              this.minutes = null;
              this.hours = null;
              this.message = `total seconds are ${response.data}`;
            },
            error => {
              this.message = error;
            }
          );
        } else {
          this.message = "you must enter an integer for each field";
        }
      }
    }
  }
};
</script>
<style>
.conversion {
  text-align: center;
  color: #33ff33;
  width: 100%;
  height: 100%;
}
.conversion input {
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
