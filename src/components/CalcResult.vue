<template>
  <v-container class="section">
    <v-text-field
    v-model="valueDoll"
    type="number"
      label="Valor base"
    ></v-text-field>
    <v-text-field
    v-model="cotation"
    type="number"
      label="% de desconto"
    ></v-text-field>
    <h1>Valor final: {{ `${valueDoll - (valueDoll * cotation / 100)}`.split('.')[0]
      }}.{{
         `${`${valueDoll - (valueDoll * cotation / 100)}`.split('.')[1] || 0}`.substr(0,2)
          }}</h1>
    <h1>Valor descontato: {{ `${ (valueDoll * cotation / 100)}`.split('.')[0]
      }}.{{
         `${`${ (valueDoll * cotation / 100)}`.split('.')[1] || 0}`.substr(0,2)
          }}</h1>
  </v-container>
</template>

<script>
export default {
  name: 'CalcResult',

  data() {
    return {
      valueDoll: 0,
      cotation: 7,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
}
</style>
