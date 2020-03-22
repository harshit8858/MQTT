import paho.mqtt.client as mqtt
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.utils import request_type, jsontype
from django.views.decorators.csrf import csrf_exempt

client = mqtt.Client("C1")  # Client 1
client.connect("broker.hivemq.com")  # MQTT server


class checkMQTTApi(APIView):
    # @csrf_exempt
    def post(self, request):
        try:
            data = request_type(request)
            flag = int(data['flag'])
            # client.loop_start()  # start the loop
            client.subscribe("home_mqtt_topic/1")
            if flag == 1:
                client.publish("home_mqtt_topic/1", "ON")
                msg = 'ON'
            else:
                client.publish("home_mqtt_topic/1", "OFF")
                msg = 'OFF'
            # client.loop_stop()  # stop the loop
            status = 1
        except Exception as e:
            print(e)
            status = 0
            msg = 'Something went wrong!'
        return Response({'status': status, 'msg': msg})
