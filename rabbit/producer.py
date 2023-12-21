import pika
import argparse


def main(text_message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = connection.channel()
    channel.exchange_declare(exchange="logs", exchange_type="fanout", durable=True)
    channel.basic_publish(exchange="logs", routing_key="", body=text_message)

    connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument: text_message")
    parser.add_argument("-t", dest="text_message", default="Hello", type=str)

    args = parser.parse_args()
    main(args.text_message)
