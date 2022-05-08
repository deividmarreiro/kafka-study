# 📘 Apache Kafka Study with Python and Go

![License](https://img.shields.io/github/license/avcaliani/aws-app?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.10.+-yellow.svg)
![#](https://img.shields.io/badge/Go-1.18.1+-blue)

This was my learning of apache Kafka Using Go and Python

My [Notion](https://www.notion.so/Apache-Study-5e54d7a4150b4d16964bdb516d0a3620) with my journey!

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

### Create the ``purchase-topic``
```bash
# Create Topic
./kafka-utils.sh --create-topic "purchase-topic"

# Check if the topic was created
./kafka-utils.sh --describe-topic "purchase-topic"
```


### Related Links
#### Shell Script Study
- [How to Use Command Line Arguments in a Bash Script](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script)
- [Bash getopts](https://www.computerhope.com/unix/bash/getopts.htm)
- [Parse Command Line Arguments in Bash](https://www.baeldung.com/linux/bash-parse-command-line-arguments)
- [For Loop](https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script)

#### Kafka Study
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)
- [Medium: Aprendendo Kafka](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Kafka Cheat Sheet](https://github.com/lensesio/kafka-cheat-sheet)

#### Python
- [Faker](https://faker.readthedocs.io/en/master/index.html)
- [Toy Products on Amazon](https://www.kaggle.com/datasets/PromptCloudHQ/toy-products-on-amazon)
- [How to parse a Python Class to Dict ](https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json)