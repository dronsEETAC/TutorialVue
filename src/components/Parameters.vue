<template>
    <div class="popup">
        <div class="popup-inner">
            <h1 style="text-align: center ; margin-bottom: 5%">Parameters</h1>
           
            <div>
                
                <b-form-group
                    label="Name:"
                    label-for="nested-street"
                    label-cols-sm="3"
                    label-align-sm="right"   
                >
                <b-form-input id="nested-street" v-model="name"></b-form-input>
                </b-form-group>

                <b-input-group  style = "width:80%; margin-left: 10%" >
                    <b-form-input  v-model = "speed" type="range" min="0" max="100"></b-form-input>
                    <h4 >Speed: {{speed}}</h4>
                </b-input-group>

                <div style = "display: flex">
                    <div style = "width: 45%; margin: 1%">
                        <b-card bg-variant="light">
                        <b-form-group 
                            label="RadioButton Options:" 
                            label-align-sm="right"
                            v-slot="{ ariaDescribedby }"> 
                        <b-form-radio-group
                            class="pt-2"
                            :options="['Air', 'Courier', 'Mail']"
                            :aria-describedby="ariaDescribedby"
                            v-model="radioButtonSelected"
                        ></b-form-radio-group>
                        </b-form-group>
                        </b-card>
                    </div>
                    <div style = "width: 45%; margin: 1%">
                        <b-card bg-variant="light" inline>
                        <b-form-group label="CheckBox Options:" v-slot="{ ariaDescribedby }"> 
                        <b-form-checkbox-group
                            
                            id="checkbox-group-1"
                            v-model="selected"
                            :aria-describedby="ariaDescribedby"
                            name="flavour-2"
                            :options="checkBoxOptions"
                            stacked
                        >
                        </b-form-checkbox-group>
                        </b-form-group>
                        </b-card>
                    </div>
                </div>


    
            </div>

        <b-button style="width:30%;margin-left:20%" @click="writeParameters" variant="warning" size = "lg">Send parameters</b-button>
        <b-button style="width:20%;margin-left:10%" @click="close" variant="danger" size = "lg">Close</b-button>

        </div>
    </div>
</template>

<script>
import {ref} from 'vue'
export default {
    setup (props,context) {
        let name = ref (undefined)
        let speed = ref (undefined)
        let radioButtonSelected = ref (undefined)
        let checkBoxOptions= ref ( [
          { text: 'Orange', value: 'orange' },
          { text: 'Apple', value: 'apple' },
          { text: 'Pineapple', value: 'pineapple' },
          { text: 'Grape', value: 'grape'},
         { text: 'Otro', value: 'otro'}
        ]);
        let selected = ref (undefined)
        function close() {
            context.emit('close')  
        }
        function writeParameters () {
            console.log ('name: ', name.value)
            console.log ('speed: ', speed.value)
            console.log ('radioButtonSelected: ', radioButtonSelected.value)
            console.log ('selected: ', selected.value)
        }
        

        return {
            close,
            writeParameters,
            radioButtonSelected,
            name,
            speed,
            checkBoxOptions,
            selected
        }
    }
}
</script>

<style scoped>
.popup {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
  
	z-index: 99;
	background-color: rgba(0, 0, 0, 0.2);
	
	display: flex; 
	align-items: center;
	justify-content: center;
	
}
.popup-inner {
		background: #FFF;
		padding: 32px;
        width: 800px;
        height: 600px;
}
</style>