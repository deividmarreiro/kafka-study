package main

import (
	"fmt"
	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {

	const KafkaTopic = "purchase-topic"
	const KafkaHost = "localhost:9092"

	c, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": KafkaHost,
		"group.id":          "go-group",
		"auto.offset.reset": "earliest",
	})

	if err != nil {
		panic(err)
	}

	c.SubscribeTopics([]string{KafkaTopic}, nil)

	fmt.Printf("Ctrl + C to Stop!")

	for {
		msg, err := c.ReadMessage(-1)
		if err == nil {
			fmt.Printf("Message on %s: %s\n", msg.TopicPartition, string(msg.Value))
		} else {
			// The client will automatically try to recover from all errors.
			fmt.Printf("Consumer error: %v (%v)\n", err, msg)
		}
	}

	c.Close()
}
