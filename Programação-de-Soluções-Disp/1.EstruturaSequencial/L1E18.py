# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
size_file=float(input("arquivo em MB: "))
speed_net=float(input("Velocidade net em Mbps: "))
print(str((size_file/speed_net)/60))