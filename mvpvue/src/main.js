import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

// main.js
const inputCity = document.getElementById('inputCity');
const weatherInfo = document.getElementById('weatherInfo');

inputCity.addEventListener('change', fetchWeather);

function fetchWeather() {
  const city = inputCity.value.trim();

  if (city !== '') {
    axios
      .get(`http://localhost:5000/weather?city=${city}`)
      .then((response) => {
        const data = response.data;
        const weatherText = `City: ${data.city}\nTemperature: ${data.temperature}°C\nDescription: ${data.description}`;
        weatherInfo.textContent = weatherText;
      })
      .catch((error) => {
        console.error('Error fetching weather data:', error);
      });
  }
}
