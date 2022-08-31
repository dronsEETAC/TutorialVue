<template>

        <div class="popup">
            <div class="popup-inner">
        
                <div  id="map"></div>
                <b-button style="width:20%;margin-left:1%; margin-top:5%" @click="close" variant="danger" size = "lg">Close</b-button>
            </div>
        </div>


</template>

<script>
import { onMounted, ref} from 'vue'
import leaflet from 'leaflet'
export default {
    setup (props,context) {
        let map;
        let popup = leaflet.popup();
        let count = 0;
        let waypoints = ref([]);
        onMounted (() => {
             map = leaflet.map('map').setView([41.276486, 1.9886], 13);
             /* leaflet.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                 maxZoom: 21,
                 attribution: '© OpenStreetMap'
             }).addTo(map);  */
             
            let token =  "pk.eyJ1IjoibWlndWVsdmFsZXJvIiwiYSI6ImNsMjk3MGk0MDBnaGEzdG1tbGFjbWRmM2MifQ.JZZ6tJwPN28fo3ldg37liA";
        
            leaflet.tileLayer('https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}@2x.png?access_token='+token, {
                maxZoom: 23,
                attribution: 'Mapbox'
            }).addTo(map);
            map.on('click', onMapClick);
            map.on('mousemove', onMapOver);
            map.on('contextmenu', onRightClick);
         

             

        })

        function close() {
            context.emit('close')  
        }
        function onMapClick(e) {
            count = count+1;
            console.log (e.latlng)
            waypoints.value.push (e.latlng);
            if (waypoints.value.length > 1)
                leaflet.polyline(waypoints.value, {color: 'red'}).addTo(map);
            leaflet.marker(e.latlng).addTo(map).bindTooltip(count.toString(),  {
                            permanent: true,
                            direction: 'center',
                            className: "my_labels"
                         });
        
        }
        function onMapOver(e) {
            if (count> 0){
                let last = waypoints.value[waypoints.value.length-1];
                let distance = last.distanceTo(e.latlng).toFixed(0)/1000;
                
                popup
                .setLatLng(e.latlng)
                .setContent( distance.toString())
                .openOn(map);
            }
            
           
        }
        function onRightClick (e) {
            leaflet.polyline(waypoints.value, {color: 'green'}).addTo(map);
        }
        

        return {
            close,
            onMapClick,
            onMapOver,
            map,
            popup,
            count,
            waypoints
        }
    }
}
</script>

<style>
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
        width: 1900px;
        height: 900px;
}

#map { 
 width: 80%;
 height: 600px;
 border-style: solid;
}
.my_labels{
    background-color: yellow;
}
</style>