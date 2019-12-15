import boto3
import json
import sqlite3
import time

sqs = boto3.client('sqs')
queue_url = ''
conn = sqlite3.connect('play_stats.db')
c = conn.cursor()

while (True):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        WaitTimeSeconds=0
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        data = json.loads(message['Body'])

        t = (data['song_title'], data['uuid'], data['type'])
        c.execute("INSERT INTO stats VALUES (?, ?, ?)", t)
        conn.commit()

        receipt_handle = message['ReceiptHandle']

        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received message: %s' % message["Body"])
    time.sleep(1)
