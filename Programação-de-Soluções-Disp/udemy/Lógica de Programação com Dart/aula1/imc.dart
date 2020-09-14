import 'dart:async';
import 'dart:io';
main() {
  print("peso");
  var text=stdin.readLineSync();
  var peso=double.parse(text);
  print("altura");
  text=stdin.readLineSync();
  var altura=double.parse(text);
  printResult(calcImc(peso,altura));
}

printResult(double icm){
  if (icm<18.5){
    print("abaixo");
  }else if (icm>18.5&&icm<24.9) {
    print("normal");
  }else if (icm>25&&icm<29.9) {
    print("sobrepeso");
  } else if (icm>30&&icm<34.9) {
    print("obeso 1");
  } else if (icm>35&&icm<39.9) {
    print("obeso 2");
  } else {
    print("obeso 3");
  }
}

calcImc(double peso,double altura){
  return peso/(altura*altura);
}