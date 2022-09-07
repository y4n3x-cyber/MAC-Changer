#Importando subprocess

import subprocess

#Criando o objeto

if __name__ == "__main__": 
    interface = "eth0"
    new_mac = "22:33:12:43:55:88"

#Passando os parâmetros para o subprocess para desligar a interface de rede
    
    print("Desligando a interface")
    subprocess.run(["ifconfig", "eth0", "down"])

#Alterando o valor do mac para a variável new_mac 

    print("Alterando o endereço da interface hw de: ", interface, " para ", new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

#Ligando a interface novamente

    print("Endereço MAC alterado para ", new_mac)
    subprocess.run(["ifconfig", interface, "up"])

    print("Interface de rede ligada.")


