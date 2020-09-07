
import 'dart:io';
import 'src/pessoa.dart';

Pessoa pessoa = Pessoa();

main(List<String> arguments) {
  print("Escreva seu Nome");
  pessoa.nome = stdin.readLineSync();
  print("Escreva sua idade");
  pessoa.idade = int.parse(stdin.readLineSync() );
  print("Escreva seu peso");
  pessoa.peso = double.parse(stdin.readLineSync() );
  print("Escreva sua altura");
  pessoa.altura = double.parse(stdin.readLineSync() );
  print("\n");

  print("Nome: ${pessoa.nome}");
  print("imc: ${pessoa.imc()}");
  print("maior de idade: ${pessoa.maiorDeIdade()}");

}
