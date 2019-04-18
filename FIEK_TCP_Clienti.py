import socket
 
host = "127.0.0.1"
port = 12000
BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    tcpClient.connect((host, port))
    while True:
        MESSAGE = input("Cila eshte kerkesa juaj: ")
        tcpClient.send(MESSAGE.encode("ASCII"))     
        data = tcpClient.recv(BUFFER_SIZE).decode("ASCII")
        
        print("Pergjigja nga serveri eshte : "+data)
        
        
except ConnectionRefusedError:
    print("Serveri nuk ka filluar ende..")

except ConnectionResetError:
    print("Serveri eshte ndalur..")

except ConnectionAbortedError:
    print("Kjo lidhje server-klient eshte shkeputur!")
tcpClient.close()
