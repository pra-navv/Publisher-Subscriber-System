from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structure to store topics and subscribers
subscriptions = {}


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    topic_id = data.get('topicId')
    subscriber_id = data.get('subscriberId')

    if not topic_id or not subscriber_id:
        return jsonify({'error': 'Missing topicId or subscriberId'}), 400

    if topic_id not in subscriptions:
        subscriptions[topic_id] = set()

    subscriptions[topic_id].add(subscriber_id)

    return jsonify({'message': f'Subscriber {subscriber_id} subscribed to {topic_id}'}), 200


@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    topic_id = data.get('topicId')

    if not topic_id:
        return jsonify({'error': 'Missing topicId'}), 400

    if topic_id not in subscriptions:
        return jsonify({'message': 'No subscribers for this topic'}), 200

    subscribers = list(subscriptions[topic_id])

    return jsonify({'message': f'Notified subscribers of {topic_id}', 'subscribers': subscribers}), 200


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    topic_id = data.get('topicId')
    subscriber_id = data.get('subscriberId')

    if not topic_id or not subscriber_id:
        return jsonify({'error': 'Missing topicId or subscriberId'}), 400

    if topic_id in subscriptions and subscriber_id in subscriptions[topic_id]:
        subscriptions[topic_id].remove(subscriber_id)
        return jsonify({'message': f'Subscriber {subscriber_id} unsubscribed from {topic_id}'}), 200

    return jsonify({'message': f'Subscriber {subscriber_id} not found in {topic_id}'}), 404


if __name__ == '__main__':
    app.run(debug=True)
