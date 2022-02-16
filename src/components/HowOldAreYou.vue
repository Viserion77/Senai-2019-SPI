<template>
  <v-container class="section">
    <h1>Idade: {{ calculaIdade(picker) }}</h1>
    <v-date-picker v-model="picker" dark></v-date-picker>
  </v-container>
</template>

<script>
export default {
  name: 'HowOldAreYou',

  data() {
    return {
      picker: (
        new Date(
          Date.now() - (new Date()).getTimezoneOffset() * 60000,
        )
      ).toISOString().substr(0, 10),
    };
  },

  methods: {
    calculaIdade(dataNasc) {
      const dataAtual = new Date();
      const anoAtual = dataAtual.getFullYear();
      const anoNascParts = `${dataNasc}`.split('-');
      const diaNasc = anoNascParts[2];
      const mesNasc = anoNascParts[1];
      const anoNasc = anoNascParts[0];
      let idade = anoAtual - anoNasc;
      const mesAtual = dataAtual.getMonth() + 1;
      if (mesAtual < mesNasc) {
        idade -= 1;
      } else if (Number(mesAtual) === Number(mesNasc)) {
        if (new Date().getDate() < diaNasc) {
          idade -= 1;
        }
      }

      return idade;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
}
</style>
