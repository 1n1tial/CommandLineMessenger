import subprocess
import socket
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

POWERSHELL_PATH = "powershell.exe"  # POWERSHELL EXE PATH
ps_script_path =  dir_path+'\\'+'balloon-tip.ps1'

def send_balloon_tip(title, message):
    try:        
        # Execute the PowerShell command
        subprocess.run([POWERSHELL_PATH, "-File", ps_script_path, "&ShowBalloonTipInfo -Title 'Title' -Text 'Text' -Icon 'Info'"],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, check=True)
        print("Balloon tip sent successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error sending balloon tip: {e}")

def main():
    host = '127.0.0.1'  # Server's IP address
    port = 5555  # Server's port number

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Connected to server.")

        while True:
            message = input("Enter message to send (type 'exit' to close): ")
            client_socket.send(message.encode('utf-8'))

            if message.lower() == 'exit':
                break

            # Receive echo from the server
            received = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {received}")
            
            # Send balloon tip with received message
            send_balloon_tip("Server Message", received)

    except ConnectionRefusedError:
        print("Server is not available.")
    except KeyboardInterrupt:
        print("\nClosing client.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
