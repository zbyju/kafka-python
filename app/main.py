import socket
from .libs import kafka_protocol as kafka


def handle_client(client):
	client.recv(1024)
	header = kafka.HeaderV0(7)
	body = kafka.Body("")
	message = kafka.Message(header, body)
	client.sendall(message.encode())
	client.close()


def main():
	server = socket.create_server(("localhost", 9092), reuse_port=True)

	while True:
		client, addr = server.accept()
		handle_client(client)


if __name__ == "__main__":
	main()
