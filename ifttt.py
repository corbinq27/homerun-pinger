import requests
import logging

IFTTT_KEY  = ""
URL_FORMAT = "https://maker.ifttt.com/trigger/%s/with/key/%s"
EVENT      = "homerun_offline"
HOMERUN_URL= "http://192.168.0.140"

logger = logging.getLogger('homerunpinger')
handler = logging.FileHandler('/var/tmp/homerunpinger.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def fire_ifttt():
    logger.warn("can't contact homerun. Sending notification to IFTTT...")
    request_to_trigger_ifttt = requests.get(URL_FORMAT % (EVENT, IFTTT_KEY))
    logger.warn("request to IFTTT sent.  IFTTT request: %s" % request_to_trigger_ifttt.text)

try:
    request_for_homerun_online = requests.get(HOMERUN_URL+"lflflflflflfl")
    if request_for_homerun_online.status_code != 200:
        fire_ifttt()
    else:
        logger.info("Homerun is online.")
except e:
    fire_ifttt()
