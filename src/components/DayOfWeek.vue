<template>
  <v-container class="section">
    <h1>{{
      new Date(new Date(picker).setDate(
        new Date(picker).getDate()+1
      )).toLocaleString('pt-br',{ weekday: 'long' })
    }}</h1>
    <v-date-picker v-model="picker" dark></v-date-picker>
  </v-container>
</template>

<script>
export default {
  name: 'DayOfWeek',

  data() {
    return {
      picker: (
        new Date(
          Date.now() - (new Date()).getTimezoneOffset() * 60000,
        )
      ).toISOString().substr(0, 10),
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
}
</style>
