from kafka import KafkaProducer
import argparse


def main(text_message):
    producer = KafkaProducer(bootstrap_servers="localhost")
    producer.send("my_topic", text_message.encode())
    producer.flush()
    producer.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument: text_message")
    parser.add_argument("-t", dest="text_message", default="Hello", type=str)
    args = parser.parse_args()

    main(args.text_message)
