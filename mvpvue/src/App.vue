<!-- app.vue -->
<template>
  <div>
    <h1>Weather App</h1>
    <input type="text" v-model="city" placeholder="Enter city name">
    <button @click="fetchWeather">Get Weather</button>
    <pre v-if="weatherInfo">{{ weatherInfo }}</pre>
    <p v-else-if="loading">Loading...</p>
    <p v-else-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      city: '',
      weatherInfo: '',
      loading: false,
      error: '',
    };
  },
  methods: {
    fetchWeather() {
      this.weatherInfo = '';
      this.error = '';
      this.loading = true;

      axios
        .get(`http://localhost:5000/weather?city=${this.city}`)
        .then((response) => {
          const data = response.data;
          this.weatherInfo = `City: ${data.city}\nTemperature: ${data.temperature}°C\nDescription: ${data.description}`;
          this.loading = false;
        })
        .catch((error) => {
          this.error = 'Error fetching weather data';
          this.loading = false;
          console.error('Error fetching weather data:', error);
        });
    },
  },
};
</script>

<style>
/* Add your custom styles here */
</style>
