<template>
    <div class="topStyle">
        <div style = "margin-left: 20%">
       
            <b-button @click="alertClicked" style="margin: 1%; width:15%" variant="primary">Alert</b-button>
            <b-button style="margin: 1%; width:15%" variant="secondary">Secondary</b-button>
            <b-button style="margin: 1%; width:15%" variant="success">Success</b-button>
            <b-button style="margin: 1%; width:15%" variant="danger">Danger</b-button>
     
        </div>
        <b-input-group prepend="New user" style = "width:50%; margin-left: 22%; margin-top: 1%">
            <b-form-input placeholder="name here" v-model="username"></b-form-input>
            <b-form-input placeholder="age here" v-model="age"></b-form-input>
            <b-input-group-append>
            <b-button @click ="InputUsername" variant="info">Enter</b-button>
            </b-input-group-append>
        </b-input-group>
    </div>
</template>

<script>
import { defineComponent, ref,inject  } from 'vue'
import Swal from 'sweetalert2'

export default defineComponent({
    setup () {
        let username = ref(undefined);
        let age= ref(undefined);
        const emitter = inject('emitter');
        function alertClicked () {
            Swal.fire('Alert clicked')
        }
        function InputUsername () {
            console.log ('name: ', username.value, ' age: ', age.value);
            emitter.emit('newUser', {'name':username.value,'age':age.value})
            username.value = undefined;
            age.value = undefined;
        }
        

        return {
            alertClicked,
            InputUsername,
            username,
            age,emitter
        }
    }
})
</script>

<style scoped>
    .topStyle {
        border-style: solid;
        border-color: red;
        height: 20%
    }

</style>