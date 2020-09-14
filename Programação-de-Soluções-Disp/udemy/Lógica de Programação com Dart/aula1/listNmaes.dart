import 'dart:io';

main() {
  var nomes=[];
  bool condicao=true;
  while(condicao){
    print("nema:");
    String text = stdin.readLineSync();
    if (text == "sair") {
      print("saindo");
      condicao=false;
    } else {
      nomes.add(text);
    }
  }
  print(nomes);
}