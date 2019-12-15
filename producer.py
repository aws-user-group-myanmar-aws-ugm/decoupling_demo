# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


from botocore.exceptions import ClientError
from flask import Flask, request
from flask_cors import CORS, cross_origin
import boto3
import json
import logging

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def send_sqs_message(sqs_queue_url, msg_body, msg_group_id):
    """

    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :param msg_group_id: MessageGroupId
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """

    # Send the SQS message
    sqs_client = boto3.client('sqs')
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body,
                                      MessageGroupId=msg_group_id)
    except ClientError as e:
        logging.error(e)
        return None
    return msg


@app.route('/collect', methods=['POST'])
@cross_origin()
def collect():
    data = request.get_json()
    """Exercise send_sqs_message()"""

    # Assign this value before running the program
    sqs_queue_url = ''

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Send some SQS messages
    data = {
        'type': data['type'],
        'uuid': data['id'],
        'song_id': 1,
        'song_title': data['title']
    }
    msg_body = json.dumps(data)
    msg = send_sqs_message(sqs_queue_url, msg_body, 'aa-bb')
    # if msg is not None:
    #     logging.info(f'Sent SQS message ID: {msg["MessageId"]}')

    return ''
