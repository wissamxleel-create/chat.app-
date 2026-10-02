import socket

def check_port(host, port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) 
    
    result = s.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
        
    s.close()


target_host = "127.0.0.1"
target_port = 80 

check_port(target_host, target_port)