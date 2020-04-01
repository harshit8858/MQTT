import paho.mqtt.client as mqtt
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.utils import request_type
# from django.views.decorators.csrf import csrf_exempt


'''
create client > connect client > client.loop_start() > client.is_connected() = True
'''

client = mqtt.Client("clientId-8858414441")  # Client 1
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

client.on_message = on_message

client.connect("broker.mqttdashboard.com")  # MQTT server


class checkMQTTApi(APIView):
    # @csrf_exempt
    def post(self, request):
        try:
            data = request_type(request)
            flag = int(data['flag'])
            print(data['flag'])
            # client.loop_start()  # start the loop
            print("Subscribing to topic", "home_mqtt_topic/1")
            client.loop_start()
            client.subscribe("home_mqtt_topic/1")
            if flag == 1:
                client.publish("home_mqtt_topic/1", "ON")
                print("Publishing message to topic", "home_mqtt_topic/1 - ON")
                msg = 'ON'
            else:
                client.publish("home_mqtt_topic/1", "OFF")
                print("Publishing message to topic", "home_mqtt_topic/1 - OFF")
                msg = 'OFF'
            client.loop_stop()  # stop the loop
            status = 1
        except Exception as e:
            print(e)
            status = 0
            msg = 'Something went wrong!'
        return Response({'status': status, 'msg': msg})
