<template>
    <div class="popup">
        <div class="popup-inner">
            Parameters
            <b-button style="width:20%;margin-left:10%" @click="close" variant="danger" size = "lg">Close</b-button>
        </div>
    </div>
</template>

<script>
export default {
    setup (props,context) {
        function close() {
            context.emit('close')  
        }
        

        return {
            close
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