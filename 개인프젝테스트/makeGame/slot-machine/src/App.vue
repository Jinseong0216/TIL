<template>
  <div id="app">
    <SlotMachine />
  </div>
</template>

<script>
import SlotMachine from './components/SlotMachine.vue';

export default {
  components: {
    SlotMachine,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
