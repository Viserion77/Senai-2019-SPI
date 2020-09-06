import 'dart:io';
main() {
  print("peso");
  var text=stdin.readLineSync();
  var peso=double.parse(text);
  print("altura");
  text=stdin.readLineSync();
  var altura=double.parse(text);
  var calc=peso/(altura*altura);
  if (calc<18.5){
    print("abaixo");
  }else if (calc>18.5&&calc<24.9) {
    print("normal");
  }else if (calc>25&&calc<29.9) {
    print("sobrepeso");
  } else if (calc>30&&calc<34.9) {
    print("obeso 1");
  } else if (calc>35&&calc<39.9) {
    print("obeso 2");
  } else {
    print("obeso 3");
  }
}