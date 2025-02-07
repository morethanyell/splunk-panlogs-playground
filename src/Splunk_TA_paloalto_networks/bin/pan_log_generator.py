import random
import datetime
import time
import ipaddress
import socket

def generate_random_public_ipaddr():
    """Generates a random public IPv4 address, avoiding private and reserved ranges."""
    while True:
        ip = ipaddress.IPv4Address(random.randint(1, 0xFFFFFFFF))
        if not (ip.is_private or ip.is_reserved or ip.is_loopback or ip.is_multicast):
            return str(ip)

def generate_random_rfc1918_ipaddr():
    """Generates a random private IPv4 address following RFC 1918."""
    private_ranges = [
        (10, random.randint(0, 255), random.randint(0, 255), random.randint(1, 254)),  # 10.0.0.0/8
        (172, random.randint(16, 31), random.randint(0, 255), random.randint(1, 254)), # 172.16.0.0/12
        (192, 168, random.randint(0, 255), random.randint(1, 254))                     # 192.168.0.0/16
    ]
    return ".".join(map(str, random.choice(private_ranges)))

def generate_random_pan_log():
    """Generates a single fake Palo Alto Networks traffic log entry."""
    
    receive_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    generated_time = (datetime.datetime.now() - datetime.timedelta(seconds=random.randint(1, 30))).strftime("%Y/%m/%d %H:%M:%S")
    start_time = (datetime.datetime.now() - datetime.timedelta(seconds=random.randint(10, 120))).strftime("%Y/%m/%d %H:%M:%S")
    
    log_type = random.choice(["SYSTEM", "TRAFFIC", "THREAT"])
    
    serial_number = f"{random.randint(100000000000, 999999999999)}"
    session_id = random.randint(100000, 999999)
    
    src_ip = generate_random_rfc1918_ipaddr()
    dest_ip = generate_random_public_ipaddr()
    
    src_port = random.randint(1024, 65535)
    dest_port = random.choice([80, 443, 53, 22, 3389, random.randint(1024, 65535)])  # Common + random port
    
    app = random.choice(["web-browsing", "ssl", "dns", "ssh", "ftp", "unknown-tcp"])
    action = random.choice(["allow", "deny", "drop"])
    
    bytes_sent = random.randint(500, 50000)
    bytes_received = random.randint(500, 50000)
    packets = random.randint(5, 500)
    
    source_zone = random.choice(["Trust", "Untrust", "DMZ"])
    destination_zone = random.choice(["Untrust", "Trust", "DMZ"])
    
    category = random.choice(["networking", "file-sharing", "malware", "proxy-avoidance"])
    
    country_src = random.choice(["United States", "Germany", "Japan", "Philippines", "Brazil"])
    country_dest = random.choice(["United States", "China", "Russia", "India", "France"])
    
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0)", 
        "curl/7.68.0", 
        "python-requests/2.31.0", 
        "wget/1.21.1"
    ])
    
    # Creating a fake Palo Alto log entry
    log_entry = [
        "", receive_time, serial_number, log_type, "", generated_time,
        src_ip, dest_ip, "203.0.113.5", dest_ip, "Fake_Rule",
        "admin", "", app, "vsys1", source_zone, destination_zone,
        "ethernet1/1", "ethernet1/2", "log", generated_time,
        session_id, 1, src_port, dest_port, random.randint(1024, 65535),
        dest_port, "0x0", 6, action, bytes_sent + bytes_received,
        bytes_sent, bytes_received, packets, start_time, 
        random.randint(1, 300), category, random.randint(1000000, 9999999),
        "0", country_src, country_dest, "", "", "", "",
        "", user_agent, "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", ""
    ]
    
    return ",".join(map(str, log_entry))  

def generate_pan_logs_live():
    
    hostname = socket.gethostname()  
    
    try:
        while True:
            log_entry = generate_random_pan_log()
            
            timestamp = datetime.datetime.now().strftime("%b %e %H:%M:%S")
            
            formatted_log = f"{timestamp} {hostname} 1{log_entry}"
            
            print(formatted_log)
            
            time_interval = random.randint(1, 3)
            time.sleep(time_interval)
    
    except KeyboardInterrupt:
        print("\nStopped log generation.")

generate_pan_logs_live()
