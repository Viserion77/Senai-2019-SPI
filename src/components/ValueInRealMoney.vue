<template>
  <v-container class="section">
    <v-text-field
      v-model="valueDoll"
      type="number"
      label="Valor em dólares"
    />
    <v-text-field
      v-model="cotation"
      type="number"
      label="Cotação"
    />
    <h1>
      Valor em reais: {{ `${valueDoll * cotation}`.split(".")[0] }}.{{
        `${`${valueDoll * cotation}`.split(".")[1] || 0}`.substr(0, 2)
      }}
    </h1>
  </v-container>
</template>

<script>
export default {
  name: 'ValueInRealMoney',

  data() {
    return {
      valueDoll: 0,
      cotation: 5.2,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
}
</style>
