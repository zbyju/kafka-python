# Python Kafka Clone

A from-scratch implementation of Kafka's core functionality in Python, using only the standard library. This project aims to replicate Kafka's message brokering capabilities and protocol, providing a learning experience and a potentially lightweight alternative for specific use cases.

## Features

* **Kafka Protocol Compatibility:** Adheres to the Kafka protocol for communication, ensuring interoperability with Kafka clients.
* **Message Production and Consumption:** Implements basic message production and consumption functionality.
* **Topic Management:** Supports topic creation and management.
* **APIVersion Handling:** Handles APIVersion requests from clients.
* **Fetch Command (In Progress):** Actively working on implementing the `Fetch` command for message consumption.

## Future Goals

* **Complete Fetch Implementation:** Add support for concurrent requests, consuming messages from disk, and handling various Fetch scenarios.
* **Persistence:** Implement persistent storage for messages, ensuring durability.
* **Consumer Groups and Rebalancing:** Support consumer groups for scalable message consumption and implement rebalancing for fault tolerance.
* **Replication:** Add support for replication to ensure data availability and fault tolerance.
* **Performance Optimization:** Optimize message handling and storage for improved performance.

## Getting Started

1. **Clone the Repository:**
```bash
git clone [invalid URL removed]
```

2. **Install Dependencies:**

Ensure you have Python 3.8 and higher installed.

```bash
pip install ruff
```

3. **Run the Server:**
```bash
python -m app.main
```

4. **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests. Please adhere to the project's coding style and ensure your code passes Ruff checks.

5. **Disclaimer**
This project is a work in progress and is not intended for production use. It serves as a learning exercise and a potential foundation for further development.

6. **License**
This project is licensed under the MIT License.




[![progress-banner](https://backend.codecrafters.io/progress/kafka/41732365-cfa5-480a-ba38-3a987ee6ca43)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)