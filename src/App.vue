<template>
  <div class ="main">
    <Top></Top>
    <div style = "display: flex; height: 50%">
      <Left></Left>
      <Right></Right>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Top from './components/Top.vue';
import Left from './components/Left.vue';
import Right from './components/Right.vue';
import Bottom from './components/Bottom.vue';

export default defineComponent({
  name: 'App',
  components: {
    Top,
    Left,
    Right,
    Bottom
}
});
</script>

<style>
  .main {
    height: 900px;
  }

</style>
