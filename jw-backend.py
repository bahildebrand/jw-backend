import json
import random

wrong_reasons = [
    "Definitely.",
    "Does a bear shit in the woods?",
    "Big wrong.",
    "Bongus Wrongus.",
    "Yurp",
    "Is a frog's ass water tight?",
    "Is a bear catholic?",
    "Does the pope shit in the woods?",
    "Is the pope catholic?",
    "Does a Polish rifle shoot white flags?",
    "Is the atomic weight of Cobalt 58.9?",
    "Is the space pope reptilian?",
    "Beeg Beeg",
    "Wrongo Bongo" ]

def lambda_handler(event, context):
    idx = random.randint(0,len(wrong_reasons)-1)

    return {
        'statusCode': 200,
        'body': json.dumps({'reason': wrong_reasons[idx]})
    }
