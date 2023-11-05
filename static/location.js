// location.js
mapboxgl.accessToken = 'pk.eyJ1Ijoia3NoaXRpajYiLCJhIjoiY2xvbG4zOXU0MGYxYzJsbjNxZW9qOWdjYSJ9.MDpMb7litim97rQ5nltPLg'; // Replace with your Mapbox Access Token

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11', // Replace with your desired map style
  center: [-74.5, 40], // Initial map center (longitude, latitude)
  zoom: 9 // Initial zoom level
});

document.getElementById('get-location').addEventListener('click', function() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;

      // Reverse geocode the coordinates to get the address using a geocoding service
      var geocodingApiUrl = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + longitude + ',' + latitude + '.json?access_token=' + mapboxgl.accessToken;

      fetch(geocodingApiUrl)
        .then(response => response.json())
        .then(data => {
          var addressComponents = data.features[0].context;
          var streetName = addressComponents.find(component => component.id.startsWith('street'));
          var streetText = document.getElementById('street-text'); // Get the paragraph element

          if (streetName) {
            streetText.textContent = 'Your Street: ' + streetName.text;
          } else {
            streetText.textContent = 'Street name not found';
          }
        })
        .catch(error => {
          console.error('Error fetching address:', error);
        });
    });
  } else {
    alert('Geolocation is not supported in your browser.');
  }
});
