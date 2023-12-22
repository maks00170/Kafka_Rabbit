import sys, os
from kafka import KafkaConsumer


def main(group_id):
    consumer = KafkaConsumer(bootstrap_servers="localhost", group_id=group_id)
    consumer.subscribe(["my_topic"])

    for message in consumer:
        print(f"Received: {message.value.decode()}")
    consumer.close()


if __name__ == "__main__":
    group_id = os.environ.get('CONSUMER_GROUP', 'default-group')
    try:
        main(group_id)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
