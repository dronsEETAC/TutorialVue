<template>
  <div class="bottomStyle">Bottom</div>
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
.bottomStyle {
  border-style: solid;
  border-color: rgb(34, 255, 0);
  height: 30%
}
</style>