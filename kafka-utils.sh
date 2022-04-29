#!/bin/bash

ZOOKEEPER_URL="zookeeper:2181"
KAFKA_URL="kafka:29092"
for option in "$@"; do
  case $option in
  --help)
    echo "Utilities to use Kafka"
    echo
    echo "Parameters: "
    echo "01 - Topic Name"
    echo
    echo "Syntax: kafka-utils [--create-topic | --describe-topic | --test-prod | --test-cons ] TOPIC_NAME"
    echo "options:"
    echo "--create-topic     Create a topic if not exists in the kafka."
    echo "--describe-topic   Describe a kafka topic."
    echo "--test-prod        Test messages to kafka topic (sequence 1 to 100)."
    echo "--test-cons        Test to print the messages sent in the --test-prod."
    echo "--help             Help with the script"
    echo
    shift
    ;;

  --create-topic)
    docker-compose exec kafka kafka-topics --create \
      --zookeeper "$ZOOKEEPER_URL" \
      --replication-factor "1" \
      --if-not-exists \
      --partitions "3" \
      --topic "$2"
    shift
    ;;

  --describe-topic)
    docker-compose exec kafka kafka-topics --describe \
      --zookeeper "$ZOOKEEPER_URL" \
      --topic "$2"
    shift
    ;;
  --delete-topic)
    docker-compose exec kafka kafka-topics --delete \
      --zookeeper "$ZOOKEEPER_URL" \
      --topic "$2"
    shift
    ;;
  --test-prod)
    docker-compose exec kafka \
      bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list $KAFKA_URL --topic $2 && echo 'Produced 100 messages.'"
    shift
    ;;
  --test-cons)
    docker-compose exec kafka \
      kafka-console-consumer --bootstrap-server "$KAFKA_URL" --topic "$2" --from-beginning --max-messages 100
    shift
    ;;
  esac
done
