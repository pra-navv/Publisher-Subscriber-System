Publisher-Subscriber Notification System
This project implements a simple Publisher-Subscriber Notification System using Flask.

API Endpoints:

1)Subscribe to a Topic URL: /subscribe

Method: POST

Body: { "topicId": "topic1", "subscriberId": "subscriber1" }

Response : { "message": "Subscriber subscriber1 subscribed to topic1" }

2)Notify Subscribers

URL: /notify

Method: POST Body:{ "topicId": "topic1" }

Response:{ "message": "Notified subscribers of topic1", "subscribers": ["subscriber1"] }

3)Unsubscribe from a Topic

URL: /unsubscribe

Method: POST Body:{ "topicId": "topic1", "subscriberId": "subscriber1" }

Response:{ "message": "Subscriber subscriber1 unsubscribed from topic1" }
