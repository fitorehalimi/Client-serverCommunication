from socket import *

host = "127.0.0.1"
port = 12000


udpClient = socket(family=AF_INET, type=SOCK_DGRAM)
udpClient.settimeout(5)


while True:
    try:
        kerkesa=input("Cila eshte kerkesa juaj: ")
        udpClient.sendto(kerkesa.encode("ASCII"),(host,port))
        pergjigja, addressa = udpClient.recvfrom(2048)
        print("Pergjigja nga serveri eshte : "+pergjigja.decode("ASCII"))
    except ConnectionError:
        print("\tLidhja me sererin nuk eshte e mundur.")
    except TimeoutError:
        print("\tKerkesa juaj deshtoi te dergohej.")
connectionSocket.close()

clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)
clientSocket.settimeout(5)
 