import socket

def port_scan(target_host, target_ports):
    for port in target_ports:
        # Yeni bir soket oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Belirtilen porta bağlanmayı dene
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port}: Açık")
        else:
            print(f"Port {port}: Kapalı")
        
        # Soketi kapat
        sock.close()

# Kullanıcıdan hedef IP adresini al
target_host = input("Hedef IP adresini girin: ")

# Kullanıcıdan hedef portları al
target_ports = input("Taranacak portları virgülle ayırarak girin: ").split(",")

# Port taramasını başlat
port_scan(target_host, target_ports)
