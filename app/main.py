import socket
import threading
from .libs import kafka_protocol as kafka


def handle_client(client: socket.socket):
	while True:
		request = client.recv(2048)

		header = kafka.HeaderV2.decode(request)
		body = kafka.Body("")
		message = kafka.Message(header, body)
		client.sendall(message.encode())


def main():
	server = socket.create_server(("localhost", 9092), reuse_port=True)

	while True:
		client, addr = server.accept()
		threading.Thread(target=handle_client, args=(client,)).start()


if __name__ == "__main__":
	main()
