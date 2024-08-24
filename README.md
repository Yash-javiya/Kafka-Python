# Kafka-Python Learning Project

## Project Overview

This repository is designed as a learning project to develop and enhance skills in working with Apache Kafka using Python. The project covers the fundamental concepts of Kafka, including producing and consuming messages using the Kafka-Python library. The use of Docker for setting up Kafka instances further enriches the learning experience.

## Project Structure

- **producer.py**: This script contains the implementation of a Kafka producer that sends messages to a Kafka topic.

- **consumer.py**: This script contains the implementation of a Kafka consumer that reads messages from a Kafka topic.

- **docker-compose.yml**: This file is used to set up a Kafka and Zookeeper instance using Docker. It allows you to easily bring up a Kafka environment without needing to install it directly on your machine.

- **requirements.txt**: Lists the dependencies required to run the Kafka producer and consumer scripts.

- **.gitignore**: Specifies intentionally untracked files to ignore, including the `.venv` directory.

## Getting Started

### Prerequisites

- **Python**: Ensure that Python 3.x is installed on your machine.
- **Docker**: Docker should be installed and running.

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Yash-javiya/Kafka-Python.git
    cd Kafka-Python
    ```

2. Set up a Python virtual environment:

    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:

    - On **Windows**:

        ```sh
        .venv\Scripts\activate
        ```

    - On **macOS/Linux**:

        ```sh
        source .venv/bin/activate
        ```

4. Install the required Python packages within the virtual environment:

    ```sh
    pip install -r requirements.txt
    ```

5. Set up Kafka and Zookeeper using Docker:

    ```sh
    docker-compose up -d
    ```

### Running the Kafka Producer and Consumer

1. **Run the Producer**:

    ```sh
    python producer.py
    ```

   This will start sending messages to the Kafka topic.

2. **Run the Consumer**:

    ```sh
    python consumer.py
    ```

   This will start consuming messages from the Kafka topic.

### Example Output

#### Producer Output

When running `producer.py`, the following output indicates that messages are being successfully delivered to the Kafka topic:

``` cmd
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
Message delivered to test-topic [0]
```

#### Consumer Output

When running `consumer.py`, you may encounter the following output:

``` cmd
Received message: Message 0 from test-topic [0]
Received message: Message 1 from test-topic [0]
Received message: Message 2 from test-topic [0]
Received message: Message 3 from test-topic [0]
Received message: Message 4 from test-topic [0]
Received message: Message 5 from test-topic [0]
Received message: Message 6 from test-topic [0]
Received message: Message 7 from test-topic [0]
Received message: Message 8 from test-topic [0]
Received message: Message 9 from test-topic [0]
```

**Explanation**:

- The consumer successfully receives messages, as indicated by the "Received message" lines.
- However, the consumer also logs errors related to connection issues with the Kafka broker, potentially due to incorrect security settings or an incompatible API version.

### Stopping the Kafka Services

To stop the Kafka and Zookeeper services, run:

```sh
docker-compose down
```

### Deactivating the Virtual Environment

After you are done working, you can deactivate the virtual environment with:

```sh
deactivate
```

## Learning Objectives

- Understand and implement basic Kafka producer and consumer functionality in Python.
- Learn how to use Docker to set up a Kafka environment for development and testing.
- Gain hands-on experience in working with Kafka topics, partitions, and message offsets.
- Learn how to manage Python dependencies in a virtual environment.

## Contributing

Contributions are welcome! If you have any ideas to improve this project or find any issues, please feel free to open an issue or submit a pull request.
