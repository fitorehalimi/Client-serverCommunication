from socket import *
from datetime import datetime
import random
from math import sqrt


udp_port = 12000
host = "127.0.0.1"

serverSocket = socket(AF_INET, SOCK_DGRAM)

print("                                     ")
print("**     **Ky eshte  Serveri**       **")
print("                                     ")
print("               UDP                   ")
print("                                     ")


serverSocket.bind(('',udp_port))
print("\nPorti ne te cilin sherben serveri eshte %s" %(udp_port))


print("\n\nPrisni tani serveri do t'ju sherbej...")

while True :
    try:
        data,adresa = serverSocket.recvfrom(128)
        data = data.decode("ASCII")
        data = data.lower()
        print("\nKjo eshte kerkesa e klientit: ", data)

        ipKlientit = adresa[0]
        portiKlientit = adresa[1]
        hosti = gethostname()
               
        pergjigja = "Pershendetje!"

        def IpAddr():
            pergjigja = "IP Addresa e klientit : %s" % (ipKlientit) 
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def portNr():
            pergjigja = "Porti i klientit eshte : %s" % (portiKlientit)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def bashketingellore():
            nrBashketingelloreve = 0
            bashketingelloret = ['B','C','Ç','D','Dh','F','G','Gj','H','J','K','L','LL','M','N','Nj','P','Q','R','Rr','S','Sh','T','Th','V','X','Xh','Z','Zh','d',
                                 'z','zh','x','xh','g','gj','dh','v','b','m','n','nj','j','l','ll','r','rr','t','s','sh','c','ç','q','k','th','f','p','h']
            try:
                teksti = data[data.index(' '):]
                for i in range(0, len(teksti)):
                    if(teksti[i] in bashketingelloret):
                       nrBashketingelloreve += 1
                pergjigja = "Ky tekst "+teksti+" permban "+str(nrBashketingelloreve)+" bashketingellore."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kjo qe keni kerkuar nuk eshte tekst (ex. bashketingellore InxhinieriKompjuterike)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def printimi():
            try:
                teksti = data[data.index(' '):].strip()
                pergjigja = str(teksti)
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kjo qe keni kerkuar nuk eshte tekst (ex. printo InxhinieriKompjuterike)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def host():
            pergjigja = "Emri i kompjuterit eshte: %s" % (hosti)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def koha():
            pergjigja = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def loja():
            klientloja = []
            for i in range(0,7):
                number = random.randint(1,49)
                klientloja.insert(i, number)
            pergjigja = str(klientloja)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def fibonacci():
            try:
                number = int(data[data.index(' '):])
                def F(n):
                    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
                if number == 0:
                    f = 0
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
                elif number == 1:
                    f = 1
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
                else:
                    f = F(number-1)+F(number-2)
                    f = int(f)
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kjo qe keni kerkuar nuk ka numer(ex. fibonacci 6)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        
                    
        def sqarimet():
            pergjigja = "Metodat e serverit\n\nMetoda:\t\tPershkrimi\t\t\t\t\tSintaksa:"\
                        "\n\nIpAddr\t\tKthen IP Adresen e klientit\t\t\tIP (ip)"\
                        "\nPortNr\t\tKthen Portin e klientit\t\t\t\tPORT (port)"\
                        "\nBashketingellore\t\tGjene numrin e bashketingelloreve ne tekst\t\tBashketingellore{hapesire}Teksti (bashketingellore{hapesire}Teksti)"\
                        "\nPrinto\t\tShtyp fjalin e derguar\t\t\t\tPRINTO{hapesire}Teksti (printo{hapesire}Teksti)"\
                        "\nHost\t\tKthen emrin e kompluterit\t\t\t\tHOST (host)"\
                        "\nKoha\t\tKthen kohen aktuale ne server\t\t\tTIME (koha)"\
                        "\nLoja\t\tKthen 7 numra te rastesishem nga 1 deri 49\tLOJA (loja)"\
                        "\nFibonacci\tGjene numrin Fibonacci nga numri i dhene\tFIBONACCI{hapesire}numri (fibonacci{hapesire}numri)\n\n"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)


        if data == 'ip':
            IpAddr()
        elif data == 'port':
            portNr()
        elif data.split(' ')[0] == 'bashketingellore':
            bashketingellore()                    
        elif data.split(' ')[0] == 'printimi':
            printimi()
        elif data == 'host':
            host()
        elif data == 'koha':
            koha()
        elif data == 'loja':
            loja()
        elif data.split(' ')[0] == 'fibonacci':
            fibonacci()
        elif data == 'sqarimet':
            sqarimet()
        elif type(data) =="NULL":
            pergjigja = "Kerkesa juaj eshte gabim, udhzoheni te sqarimet!"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        else:
            pergjigja = "Kerkesa juaj eshte gabim, udhzoheni te sqarimet!"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
    except SyntaxError:
        pergjigja = "Serveri nuk ka filluar ende.."
        serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
