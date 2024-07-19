import random
import string
import sys
import pywifi
from pywifi import const
import psutil
import socket

def load_words(arquivo):
    with open(arquivo, 'r') as f:
        words = [line.strip() for line in f]
    return words

def generate_random_string(length, max_length):
    chars = string.ascii_letters + string.digits
    max_length = min(max_length, length)
    return ''.join(random.choice(chars) for _ in range(max_length))

def modify_words(words, max_suffix_length):
    modified_words = []
    for word in words:
        random_suffix = generate_random_string(len(word), max_suffix_length)
        modified_word = word + random_suffix
        modified_words.append(modified_word)
    return modified_words

def save_modified_words(modified_words, exit_file):
    with open(exit_file, 'w') as f:
        for modified_word in modified_words:
            f.write(modified_word + '\n')

def main():
    word_file = 'words.txt'
    exit_file = '388worlist.txt'
    max_suffix_length = 5

    words = load_words(word_file)

    modified_words = modify_words(words, max_suffix_length)

    save_modified_words(modified_words, exit_file)

    print(f'Arquivo salvo em {exit_file}')

def mainn():
    word_file = 'words.txt'
    exit_file = '388list.txt'
    max_suffix_length = 5

    words = load_words(word_file)

    modified_words = modify_words(words, max_suffix_length)

    save_modified_words(modified_words, exit_file)

    print(f'Arquivo salvo em {exit_file}')


def cryptography_cesar(text, displacement):
    resultado = ''

    for char in text:
        if char.isupper():
            resultado += chr((ord(char) + displacement - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + displacement - 97) % 26 + 97)
        else:
            resultado += char
    return resultado

def get_wifi_info():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()

    if len(interfaces) == 0:
        print("Nenhuma interface Wi-Fi encontrada.")
        return

    iface = interfaces[0]
    iface.scan()
    scan_results = iface.scan_results()

    current_network = None
    for network in scan_results:
        if network.ssid == iface.status() == const.IFACE_CONNECTED:
            current_network = network
            break

    if current_network:
        print(f"SSID: {current_network.ssid}")
        print(f"BSSID: {current_network.bssid}")
        print(f"Signal: {current_network.signal}")
    else:
        print("Nenhuma rede Wi-Fi conectada ou informações não disponíveis")

def get_ethernet_info():
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for interface, addresses in addrs.items():
        if interface.lower().startswith("ethernet") or \
           interface.lower().startswith("local area connection") or \
           interface.lower().startswith("en"):
            print(f"Interface: {interface}")
            for addr in addresses:
                if addr.family == socket.AF_INET:
                    print(f"  IP Address: {addr.address}")
                    print(f"  Netmask: {addr.netmask}")
                    print(f"  Broadcast IP: {addr.broadcast}")
                elif addr.family == socket.AF_INET6:
                    print(f"  IPv6 Address: {addr.address}")
                    print(f"  Netmask: {addr.netmask}")
                    print(f"  Broadcast IP: {addr.broadcast}")
                elif hasattr(psutil, 'AF_LINK') and addr.family == psutil.AF_LINK:
                    print(f"  MAC Address: {addr.address}")

            if interface in stats:
                stat = stats[interface]
                print(f"  Speed: {stat.speed}Mbps")
                print(f"  Duplex: {'Full' if stat.duplex == psutil.NIC_DUPLEX_FULL else 'Half'}")
                print(f"  MTU: {stat.mtu}")
                print(f"  Up: {stat.isup}")



draw = ''' 
Welcome User.
        ,----,
      ,/   .`|
    ,`   .'  :                         ,--,
  ;    ;     /                       ,--.'|
.'___,/    ,'     ,---.      ,---.   |  | :
|    :     |     '   ,'\    '   ,'\  :  : '      .--.--.
;    |.';  ;    /   /   |  /   /   | |  ' |     /  /    '
`----'  |  |   .   ; ,. : .   ; ,. : '  | |    |  :  /`./
    '   :  ;   '   | |: : '   | |: : |  | :    |  :  ;_
    |   |  '   '   | .; : '   | .; : '  : |__   \  \    `.
    '   :  |   |   :    | |   :    | |  | '.'|   `----.   |
    ;   |.'     \   \  /   \   \  /  ;  :    ;  /  /`--'  /
    '---'        `----'     `----'   |  ,   /  '--'.     /
                                      ---`-'     `--'---'haas.py
'''
print('')
print(draw)

choice = int(input('''
[1] = Password manager
[2] = Cryptography
[3] = WiFi information Local
[4] = Ethernet Windows Info
[5] = Ethernet & wifi Linux info            
[6] = Exit
                   
Escolha uma opção: '''))
end = False

while end == False:
    if choice == 1:
        main()
        again = int(input("Deseja outra lista?: [1] - Sim | [2] - Não: "))
        if again == 1:
            mainn()
            end = True
        elif again == 2:
            sys.exit()
        else:
            print('error')
            end = True
    elif choice == 2:
        original_text = str(input("Qual o texto a ser criptografado?: "))
        displacement = 3

        text_cryptography = cryptography_cesar(original_text, displacement)
        print("Original Text: ", original_text)
        print("Cryptography text: ", text_cryptography)
        end = True
    elif choice == 3:
        get_wifi_info()
        end = True
    elif choice == 4:
        get_ethernet_info()
        break
    elif choice == 5:
        asks = False
        while asks == False:
            ask = int(input('''
[1] = "ifconfig" 
[2] = "ip" 
                            
[3] = Sair
Qual o comando do seu sistema operacional?: '''))
            print('')
            if ask == 1:
                import subprocess

                def get_ethernet_info():
                    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
                    print(result.stdout)

                get_ethernet_info()
                get_wifi_info()
                break
            elif ask == 2:
                import subprocess

                def get_ethernet_info():
                    result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
                    print(result.stdout)

                get_ethernet_info()
                get_wifi_info()
                break
            elif ask == 3:
                sys.exit()
            else:
                print("Por favor digite uma opção valida.")
                asks = True
            
    elif choice == 6:
        sys.exit()
    else:
        print("Por favor digite uma opção valida.")
        break