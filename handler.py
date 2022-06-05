import json


def webhook(event, context):
    request_message = json.loads(event['body'])
    derived_session_fields = ['session_id', 'user_id', 'message_id']
    if request_message['request']['command'] == 'шишки вездеход':
        print(1)
        response_message = {
            "response": {
                "text": "Привет вездекодерам!",
                "tts": "Привет вездекодерам!",
                "end_session": False
            },
            "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
            "version": request_message['version']
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response_message)
        }
    else:
        response_message = {
            "response": {
                "text": "",
                "tts": "",
                "end_session": False
            },
            "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
            "version": request_message['version']
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response_message)
        }
