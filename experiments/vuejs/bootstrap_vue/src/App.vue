<template>
  <div id="app">
    <NavBar title="Puneet" />
    <div class="centered-1">
      <Accordion />
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar";
import Accordion from "./components/Accordion";

export default {
  name: "App",
  components: {
    NavBar,
    Accordion
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}

.centered-1 {
  padding-top: 3vw;
  padding-left: 5vw;
  padding-right: 5vw;
}
</style>
