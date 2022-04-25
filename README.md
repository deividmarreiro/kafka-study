# 📘 Apache Kafka Study

![License](https://img.shields.io/github/license/avcaliani/aws-app?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.10.+-yellow.svg)

This is my journey studying Apache Kafka along with another things, like Docker and Docker Compose<br>
and some new programming languages like Go, Shell Scripting and JavaScript<br>
relearn Java 😅

My [Notion](google.com) with my journey!


## Setup
```bash
# Create Kafka and Zookeeper
docker compose up -d

# Check if the containers ar up
docker-compose ps

# Check if the zookeeper is running
docker-compose logs zookeeper | grep -i binding

# Check if the kafka is running 
# (this can take few seconds because will wait for the zookeeper start first)
docker-compose logs kafka | grep -i started
```

## Kafka-utils Script

```bash
# See the help
./kafka-utils.sh --help

Utilities to use Kafka

Parameters: 
01 - Topic Name

Syntax: kafka-utils [--create-topic | --describe-topic | --test-prod | --test-cons ] TOPIC_NAME
options:
--create-topic     Create a topic if not exists in the kafka.
--describe-topic   Describe a kafka topic.
--test-prod        Test messages to kafka topic (sequence 1 to 100).
--test-cons        Test to print the messages sent in the --test-prod.
--help             Help with the script
```

### Testing
```bash
# Create Topic
./kafka-utils.sh --create-topic "test-topic"

# Check if the topic was created
./kafka-utils.sh --describe-topic "test-topic"

# Testing Sending messages through a producer
./kafka-utils.sh --test-prod "test-topic"

# Testing Consuming messages through a consumer
./kafka-utils.sh --test-cons "test-topic"
```

# TODO
- [ ] Create a consumer in Go for the Producer
- [ ] Search for a GUI to see the Kafka Messages

### Related Links
#### Shell Script Study
- [For Loop](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script)

#### Kafka Study
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)
