<template>
  <v-container id="app">
    <marquee behavior="scroll" loop="true" direction="right" >
      <img src="https://images5.alphacoders.com/403/thumb-1920-403408.jpg" style="height: 200px;">
      <table>
        <th><tr>Name</tr><tr>Email</tr></th>
        <ts><tr>Jeferson Alves</tr><tr>jeferson_alves1@estudante.sc.senai.br</tr></ts>
      </table>
    </marquee>
1)
    <HowOldAreYou/>

    <div class="divider"/>
2)
    <ValueInRealMoney/>

    <div class="divider"/>
3)
    <DayOfWeek/>

    <div class="divider"/>
4)
    <CalcResult/>
  </v-container>
</template>

<script>
import HowOldAreYou from './components/HowOldAreYou.vue';
import ValueInRealMoney from './components/ValueInRealMoney.vue';
import DayOfWeek from './components/DayOfWeek.vue';
import CalcResult from './components/CalcResult.vue';

export default {
  name: 'App',
  components: {
    HowOldAreYou,
    ValueInRealMoney,
    DayOfWeek,
    CalcResult,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.divider {
  height: 50px;
  width: 100%;
  border-top: solid 5px #2c3e5030;
}
</style>
