import pika, sys, os


def callback(ch, method, properties, message):
    print(f"Received: {message}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="logs", exchange_type="fanout", durable=True)
    result = channel.queue_declare(queue="", exclusive=True, durable=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange="logs", queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print("[*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
