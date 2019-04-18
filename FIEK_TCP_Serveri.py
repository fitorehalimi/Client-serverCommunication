import socket
from threading import Thread
from socketserver import ThreadingMixIn
from datetime import datetime
import random
from math import sqrt


class ClientThread(Thread):

    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("Lidhje i socketes se serverit filloi per: " + ip + ":" + str(port))
 
    def run(self): 
        while True :
            try:
                data = conn.recv(128).decode("ASCII")
                data = data.lower()
                print("\nKjo eshte kerkesa e klientit: ", data)

                ipKlientit = ip
                portiKlientit = port
                hosti = socket.gethostname()
               
                pergjigja = "Pershendetje!"

                def IpAddr():
                    pergjigja = "IP Addresa e klientit : %s" % (ipKlientit) 
                    conn.send(pergjigja.encode("ASCII"))
                def portNr():
                    pergjigja = "Porti i klientit eshte : %s" % (portiKlientit)
                    conn.send(pergjigja.encode("ASCII"))
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
                        conn.send(pergjigja.encode("ASCII"))
                    except ValueError:
                        pergjigja = "Kjo qe keni kerkuar nuk eshte tekst (ex. bashketingellore InxhinieriKompjuterike)."
                        conn.send(pergjigja.encode("ASCII"))
                def printimi():
                    try:
                        teksti = data[data.index(' '):].strip()
                        pergjigja = str(teksti)
                        conn.send(pergjigja.encode("ASCII"))
                    except ValueError:
                        pergjigja = "Kjo qe keni kerkuar nuk eshte tekst (ex. printo InxhinieriKompjuterike)."
                        conn.send(pergjigja.encode("ASCII"))
                def host():
                    pergjigja = "Emri i kompjuterit eshte: %s" % (hosti)
                    conn.send(pergjigja.encode("ASCII"))
                def koha():
                    pergjigja = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                    conn.send(pergjigja.encode("ASCII"))
                def loja():
                    klientloja = []
                    for i in range(0,7):
                        number = random.randint(1,49)
                        klientloja.insert(i, number)
                    pergjigja = str(klientloja)
                    conn.send(pergjigja.encode("ASCII"))
                def fibonacci():
                    try:
                        number = int(data[data.index(' '):])
                        def F(n):
                            return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
                        if number == 0:
                            f = 0
                            pergjigja = str(f)
                            conn.send(pergjigja.encode("ASCII"))
                        elif number == 1:
                            f = 1
                            pergjigja = str(f)
                            conn.send(pergjigja.encode("ASCII"))
                        else:
                            f = F(number-1)+F(number-2)
                            f = int(f)
                            pergjigja = str(f)
                            conn.send(pergjigja.encode("ASCII"))
                    except ValueError:
                        pergjigja = "Kjo qe keni kerkuar nuk ka numer(ex. fibonacci 6)."
                        conn.send(pergjigja.encode("ASCII"))
                def konvertimi():
                    try:
                        o = data.split(' ')[1]
                        try:
                            vlera = int(data.split(' ')[2])
                            if o == 'K-H' or o == 'k-h':
                                k =( vlera * 1000 )/746
                                pergjigja = str(k)
                                conn.send(pergjigja.encode("ASCII"))
                            elif o == 'H-K' or o == 'h-k':
                                k =( vlera * 746) /1000
                                pergjigja = str(k)
                                conn.send(pergjigja.encode("ASCII"))
                            elif o == 'D-R' or o == 'd-r':
                                c = (vlera * 3.14)/180
                                pergjigja = str(c)
                                conn.send(pergjigja.encode("ASCII"))
                            elif o == 'R-D' or o == 'r-d':
                                c = (vlera * 180)/3.14
                                pergjigja = str(c)
                                conn.send(pergjigja.encode("ASCII"))
                            elif o == 'G-L' or o == 'g-l':
                                d = (vlera *3.79)/1
                                pergjigja = str(d)
                                conn.send(pergjigja.encode("ASCII"))
                            elif o == 'L-G' or o == 'l-g':
                                d=vlera/3.79
                                pergjigja = str(d)
                                conn.send(pergjigja.encode("ASCII"))
                            else:
                                pergjigja = "Provoni nje tjeter sepse ky opsion nuk ekziston!"
                                conn.send(pergjigja.encode("ASCII"))
                        except IndexError:
                            pergjigja = "Mungon vlera qe deshironi ta konvertoni!"
                            conn.send(pergjigja.encode("ASCII"))
                        except ValueError:
                            pergjigja = "Vlera qe e keni dhene duhet te jete numer i plote!"
                            conn.send(pergjigja.encode("ASCII"))
                    except IndexError:
                        pergjigja = "Ekzistojne keto opsione(ex. K-H,H-K ,k-h,h-k,D-R,R-D,d-r,r-d,g-l,l-g,G-L,L-G"\
                        "\n\t(K-KILOWATT , H-HORSEPOWER , D-DEGREES,G-GALLONS,L-LITERS,R-RADIANS). "
                        conn.send(pergjigja.encode("ASCII"))
               
                
                def sqarimet():
                    pergjigja = "Metodat e serverit\n\nMetoda:\t\tPershkrimi\t\t\t\t\tSintaksa:"\
                        "\n\nIpAddr\t\tKthen IP Adresen e klientit\t\t\tIP (ip)"\
                        "\nPortNr\t\tKthen Portin e klientit\t\t\t\tPORT (port)"\
                        "\nBashketingellore\t\tGjene numrin e bashketingelloreve ne tekst\t\tBashketingellore{hapesire}Teksti (bashketingellore{hapesire}Teksti)"\
                        "\nPrinto\t\tShtyp fjalin e derguar\t\t\t\tPRINTO{hapesire}Teksti (printo{hapesire}Teksti)"\
                        "\nHost\t\tKthen emrin e kompjuterit\t\t\t\tHOST (host)"\
                        "\nKoha\t\tKthen kohen aktuale ne server\t\t\tTIME (koha)"\
                        "\nLoja\t\tKthen 7 numra te rastesishem nga 1 deri 49\tLOJA (loja)"\
                        "\nFibonacci\tGjene numrin Fibonacci nga numri i dhene\tFIBONACCI{hapesire}numri (fibonacci{hapesire}numri)"\
                        "\nKonverto\tKonverton disa njesi\t\t\t\tKONVERTO{hapesire}OPSIONI{hapesire}numri\n\n"
                    conn.send(pergjigja.encode("ASCII"))


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
                elif data == 'LOJA' or data == 'loja':
                    loja()
                elif data.split(' ')[0] == 'fibonacci':
                    fibonacci()
                elif data.split(' ')[0] == 'konvertimi':
                    konvertimi()
                elif data == 'sqarimet':
                    sqarimet()
                elif type(data) == "NULL":
               
                   pergjigja = "Kerkesa juaj eshte gabim, udhzoheni te sqarimet!"
                   conn.send(pergjigja.encode("ASCII"))
                else:
                    pergjigja = "Kerkesa juaj eshte gabim, udhzoheni te sqarimet!"
                    conn.send(pergjigja.encode("ASCII")) 

                

            except ConnectionRefusedError:
                print("Kjo lidhje klient-server nuk eshte e mundur!")
                conn.close()
                break

            except ConnectionResetError:
                print("Kjo lidhje klient-server eshte shkeputur!")
                conn.close()
                break

            except ConnectionAbortedError:
                print("Kjo lidhje klient-server eshte shkeputur!")
                conn.close()
                break

host = "127.0.0.1"
tcp_port = 12000
threads = []

buffer = 20

print("                                     ")
print("**     **Ky eshte  Serveri**       **")
print("                                     ")
print("               TCP                   ")
print("                                     ")

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((host,tcp_port))


while True: 
    tcpServer.listen(4) 
    print("Shohim lidhje tjera nga TCP klienti...")
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join()




