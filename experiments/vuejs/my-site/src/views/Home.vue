<template>
  <div class="home">
    <h1>This is Puneet.</h1>
    <img
      alt="Puneet Reddy"
      v-bind:src="defaultPic"
      @mouseover="defaultPic=puneetOld"
      @mouseleave="defaultPic=puneetNew"
    />
    <h1>This is his site. This is his story.</h1>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      defaultPic: require('../assets/puneet_new.jpeg'),
      puneetOld: require('../assets/puneet_old.jpeg'),
      puneetNew: require('../assets/puneet_new.jpeg')
    }
  }
}
</script>
