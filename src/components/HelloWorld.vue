<template>
  <div class="hello">
    <button @click ="onButtonClick" class ="buttonStyle"> Ckick here</button>
    <h1>Message from parent: {{ msg }}</h1>
    <h1>selt message: {{ selfMessage }}</h1>
   
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  setup () {
    let selfMessage = ref ("my message");
    function onButtonClick () {
      console.log ('button clicked');
      selfMessage.value = "button clicked"
    }
    return {
      onButtonClick,
      selfMessage
    }
  }
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .buttonStyle {
    background-color: brown;
    color: white;
  }

</style>
