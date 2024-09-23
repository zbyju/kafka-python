import socket
from .libs import kafka_protocol as kafka


def handle_client(client: socket.socket):
	request = client.recv(2048)

	header = kafka.HeaderV2.decode(request)
	body = kafka.Body("")
	message = kafka.Message(header, body)
	client.sendall(message.encode())


def main():
	server = socket.create_server(("localhost", 9092), reuse_port=True)
	client, addr = server.accept()

	while True:
		handle_client(client)


if __name__ == "__main__":
	main()
