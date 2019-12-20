from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
import RPi.GPIO as GPIO
from .stats import write_msg

dht_pin = 21
ledPin = 20
led_status = 'OFF'
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(dht_pin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
# Create your views here.
  
def index(request):
        return render(request,'index.html')

def oled(request):
    if request.method == 'POST':
        msg = request.POST.get('oled')
        write_msg(msg)
        return redirect('index')
