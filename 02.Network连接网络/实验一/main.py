import network
from machine import Pin
sta_if = network.WLAN(network.STA_IF)
p2 = Pin(2, Pin.OUT)
#����������ѽ����ӿڽ��ã�����ۿ�ʵ��Ч������ʵ�����ȥ��
sta_if.active(False)
if not sta_if.isconnected():
    p2.low()
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('TurnipSmart', 'turnip2016')
    while not sta_if.isconnected():
        pass
if sta_if.isconnected():
    print('connect success')
    p2.high()
    print('network config:', sta_if.ifconfig())