<template>
    <div class="rightStyle">
        <b-table class = "myTable" :items="userList" :fields="['name', 'age', 'Delete']">
            <template v-slot:cell(Delete)="{ item }">
            <span><b-btn @click="deleteItem(item)"><i className="bi bi-trash3-fill" style='color:red'></i></b-btn></span>
            </template> 
        </b-table>
    </div>
</template>

<script>
import { defineComponent, ref, inject } from "vue";

export default defineComponent({
  setup() {
    let userList = ref ([]);
    const emitter = inject('emitter')
    emitter.on ('newUser', (user)=>{
        userList.value.push(user)
        console.log ('List ',  userList.value)
    });
    function deleteItem (item) {
        this.userList = this.userList.filter (user => user.name != item.name);
    }
    return {
        userList,
        deleteItem
    };
  },
});
</script>

<style scoped>
.rightStyle {
  border-style: solid;
  border-color: blue;
  width: 50%
}
.myTable {
    width:50%;
    margin-left: 25%;
    margin-top: 1%;
    border-style: solid;
}
</style>