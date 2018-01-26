import logging

import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_data(url=None, statistics=[]):
    out = {x["alias"]: None for x in statistics}
    r = requests.get(url)
    if r.status_code != 200:
        logger.error(
            "Error retreiving RabbitMQ statistics:\n"\
            " => Status code: {}\n"\
            " => URL: {}\n"\
            .format(r.status_code, url)
        )
    else:
        data = r.json()
        log_messages = ["Retreived the following statistics from RabbitMQ:"]
        for x in statistics:
            key = x["alias"]
            val = data[x["name"]]
            out[key] = val
            log_messages.append(" => {}: {}".format(key, val))
        if out:
            logger.debug("\n".join(log_messages))
    return out