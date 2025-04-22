#!/usr/bin/env python3

import socket

def main():
    print("Simple TCP Client")
    server_ip = input("Enter server IP (default: 127.0.0.1): ") or "127.0.0.1"
    port_input = input("Enter server port (default: 12345): ")
    try:
        server_port = int(port_input) if port_input else 12345
    except ValueError:
        print("Invalid port. Using default: 12345")
        server_port = 12345

    try:
        # Create and connect socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        # Send and receive
        message = input("Enter message to send: ")
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
