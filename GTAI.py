import socket
import struct
import hashlib
import requests
import time

def connect_to_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock

def send_packet(sock, packet):
    sock.send(packet)

def receive_packet(sock):
    return sock.recv(1024)

def solve_captcha(api_key, site_key, url):
    response = requests.post('http://2captcha.com/in.php', data={
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url,
        'json': 1
    })
    request_id = response.json().get('request')
    
    while True:
        result = requests.get('http://2captcha.com/res.php', params={
            'key': api_key,
            'action': 'get',
            'id': request_id,
            'json': 1
        }).json()
        if result.get('status') == 1:
            return result.get('request')
        time.sleep(5)

def get_ubiticket(username, password):
    url = "https://public-ubiservices.ubi.com/v3/profiles/sessions"
    headers = {
        'Ubi-AppId': 'your_app_id',
        'Ubi-RequestedPlatformType': 'uplay',
        'Content-Type': 'application/json'
    }
    data = {
        "email": username,
        "password": password
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('ticket')
    return None

def authenticate(sock, username, password, mac, rid, ubiticket):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    login_packet = struct.pack('<I', len(username) + len(password_hash) + len(mac) + len(rid) + len(ubiticket) + 5)
    login_packet += username.encode() + b'\x00' + password_hash.encode() + b'\x00' + mac.encode() + b'\x00' + rid.encode() + b'\x00' + ubiticket.encode() + b'\x00'
    send_packet(sock, login_packet)

def main():
    ip = "www.growtopiagame1.com"
    port = 17091
    
    username = "your_username"
    password = "your_password"
    mac = "your_mac_address"
    rid = "your_random_id"
    captcha_api_key = "your_2captcha_api_key"
    site_key = "growtopia_site_key"
    captcha_url = "growtopia_captcha_url"

    ubiticket = get_ubiticket(username, password)
    if not ubiticket:
        print("Failed to get UbiTicket")
        return
    
    sock = connect_to_server(ip, port)
    captcha_solution = solve_captcha(captcha_api_key, site_key, captcha_url)
    
    authenticate(sock, username, password, mac, rid, ubiticket)
    
    while True:
        packet = receive_packet(sock)
        if packet:
            print(packet)

if __name__ == "__main__":
    main()
