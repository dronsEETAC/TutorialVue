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
        <div style="display:flex">
        <div  style ="width:70%">
        <canvas style="margin-left:20%; width: 400px; height: 300px; border-style: solid;" id= "output"></canvas>
        </div> 
        <div class ="buttonColumn">
           
           <b-button style =" margin:1%" @click="mode = 'gray'" variant="info">
               Gray </b-button>
           <b-button style ="margin:1%" @click="mode = 'canny'" variant="success">
               Canny </b-button>
           <b-button style ="margin:1%" @click="mode = 'normal'" variant="warning">
               Normal </b-button>
       </div>
       </div>
    </div>
</template>

<script>
import { onMounted,defineComponent, inject, ref } from 'vue'
import * as cv from 'opencv.js'

export default defineComponent({
    setup () {
        let client = inject('mqttClient');
        let mode = ref ('normal')
        onMounted(() => {
            client.on('message', (topic, message) => {
                if (topic == 'videoFrame') {
                    const img = new Image();
                    img.src = "data:image/jpg;base64,"+message;
 
                    img.onload = () => {  
                        let dst;
                        if (mode.value == 'normal')
                            dst = cv.imread (img);
                        if (mode.value == 'gray') {
                            let mat = cv.imread (img);
                            dst = new cv.Mat();
                            cv.cvtColor (mat, dst, cv.COLOR_RGB2GRAY,0);
                            mat.delete()
                        }
                        if (mode.value == 'canny') {
                            let mat = cv.imread (img);
                            dst = new cv.Mat();
                            cv.cvtColor (mat, dst, cv.COLOR_RGB2GRAY,0);
                            cv.Canny(mat, dst, 50, 100, 3, false);
                            mat.delete()
                        }
                        cv.imshow ('output',dst);
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
            client,
            mode
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
.buttonColumn {
  display: flex;
  justify-content: center;
  flex-direction: column;
  padding-top: 20px;
  width: 20%;
  border: 2px solid red;
  padding: 10px;
  border-radius: 25px;
  margin-left: 5%
}

</style>