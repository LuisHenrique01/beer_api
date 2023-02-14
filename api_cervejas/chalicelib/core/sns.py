import os
import json
import boto3
from chalicelib.database.models import Brewery


def create_topic(data: list):
    sns = boto3.client('sns')
    sns.public(
        TargetArn=os.getenv('ARN_SNS_SAVE_BEERS'),
        Message=json.dumps({'default': json.dumps(data)}),
        MessageStructure='json'
    )


def sns_save_beers(beers: list):
    Brewery.save_many(beers)
