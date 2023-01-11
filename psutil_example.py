import psutil

def open_ports():
    open_ports = {}
    for conn in psutil.net_connections(kind='tcp'):
        if conn.status == 'ESTABLISHED':
            process = psutil.Process(conn.pid)
            process_name = process.name()
            open_ports[conn.laddr.port] = process_name
    return open_ports

ports = open_ports()
for port, process in ports.items():
    print(f"Port {port} is open and used by {process}")