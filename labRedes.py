import socket

#---------------------Cliente UDP----------------#
HOST = ''           # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    udp.sendto (msg, dest)
    msg = input()
udp.close()
#------------------------------------------------#

#------------------Servidor UDP------------------#
import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
#while True:
#    msg, cliente = udp.recvfrom(1024)
#    print (cliente, msg)
udp.close()
#------------------------------------------------#

#---------------------Cliente TCP----------------#
import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send (msg)
    msg = input()
tcp.close()
#------------------------------------------------#

#---------------------Servidor TCP---------------#
import socket
HOST = ''           # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()

#-----------------------------------------------#