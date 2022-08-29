<template>
  <div class="rightStyle">Right</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    return {};
  },
});
</script>

<style scoped>
.rightStyle {
  border-style: solid;
  border-color: blue;
  width: 50%
}
</style>