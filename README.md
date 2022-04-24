# 📘 Apache Kafka Study

![License](https://img.shields.io/github/license/avcaliani/aws-app?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.10.+-yellow.svg)

This is my journey studying Apache Kafka along with another things, like Docker and Docker Compose<br>
and some new programming languages like Go, Shell Scripting and JavaScript<br>
relearn Java 😅

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

## Create Topics

# TODO
- [ ] Learning Shell Scripting
- [ ] Create Shell script to create topics
- [ ] Create section in ReadME

### Related Links
#### Shell Script Study
- [For Loop](https://imasters.com.br/desenvolvimento/bash-for-loop-primeiro-passo-na-automacao-no-linux)

#### Kafka Study
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)