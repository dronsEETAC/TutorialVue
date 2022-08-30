<template>
    <div class = "leftStyle">
        <div>
        <b-button style ="width:20%; margin:1%; margin-left:20%"  @click="startVideoFrame" variant="success">
                Start video frame 
        </b-button>
         <b-button style ="width:20%; margin:1%" @click="stopVideoFrame" variant="warning">
                Stop video frame 
        </b-button>
        </div>
        <div  style ="width:70%">
        <canvas style="margin-left:20%; width: 400px; height: 300px; border-style: solid;" id= "output"></canvas>
        </div> 
    </div>
</template>

<script>
import { onMounted,defineComponent, inject } from 'vue'

export default defineComponent({
    setup () {
        let client = inject('mqttClient');
        onMounted(() => {
            client.on('message', (topic, message) => {
                if (topic == 'videoFrame') {
                    const img = new Image();
                    img.src = "data:image/jpg;base64,"+message;
                    const canvas = document.getElementById('output'); 
                    const context = canvas.getContext('2d');      
                    img.onload = () => {          
                        context.drawImage(
                            img,
                            0,
                            0,
                            img.width,
                            img.height,
                            0,
                            0,
                            canvas.width,
                            canvas.height
                            );  
                    };
                   
                }
            })
        })
        

        function startVideoFrame () {
            client.publish ("StartVideoStream")
            client.subscribe("videoFrame");
        }
         function stopVideoFrame () {
            client.publish ("StopVideoStream")
        }

        return {
            startVideoFrame,
            stopVideoFrame,
            client
        }
    }
})
</script>

<style scoped>
    
.leftStyle {
  border-style: solid;
  border-color: rgb(200, 255, 0);
  width: 50%
}

</style>