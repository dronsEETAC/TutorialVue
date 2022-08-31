<template>
  <button v-if = "!connected" class = "myButtonConnect" @click = "toggle">Connect</button>
  <button v-if = "connected" class = "myButtonDisconnect" @click = "toggle">Disconnect</button>
  <div v-if = "connected" class ="main">
    <Top></Top>
    <div style = "display: flex; height: 50%">
      <Left></Left>
      <Right></Right>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import { onMounted, defineComponent, ref } from 'vue';
import Top from './components/Top.vue';
import Left from './components/Left.vue';
import Right from './components/Right.vue';
import Bottom from './components/Bottom.vue';
import {io} from 'socket.io-client'
import Swal from 'sweetalert2'

export default defineComponent({
  name: 'App',
  components: {
    Top,
    Left,
    Right,
    Bottom
  },
  setup () {
    let connected = ref (false)
    const socket = io ('http://localhost:5000')
    onMounted (()=>{
      socket.on('connected', (msg) => {
          Swal.fire({
                title: "Notification on connection",
                text: msg,
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Yes"
          }).then((result) => { // <--
                if (result.value) { // <-- if confirmed
                  connected.value = true;
                }
          }); 


    });
      })
    function toggle () {
      socket.emit ('connectPlatform')
      //connected.value = !connected.value;
    }
    return {
      toggle,
      connected,
      socket
      
    }
  }
});
</script>

<style>
  .main {
    height: 900px;
  }
  .myButtonConnect {
    width : 80%;
    background-color: brown;
    color : white;
    margin-left: 10%;
    margin-bottom: 1%
  }
  .myButtonDisconnect {
    width : 80%;
    background-color: rgb(77, 42, 165);
    color : white;
    margin-left: 10%;
    margin-bottom: 1%
  }

</style>
