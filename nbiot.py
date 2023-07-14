import serial
import json
import time

with open("./settings.json","r",encoding="utf-8") as f:
    settings = json.load(f)

nbiot_serial_id = settings["nbiot_serial_id"]
server_ip = settings["server_ip"]

def connect(cmd:str, res:str=None):
    try:
        ser = serial.Serial(nbiot_serial_id, 115200)
        ser.write((cmd + "\n").encode())
        start = time.time()
        while time.time() - start < 2:
            if ser.in_waiting != 0:
                break
        if ser.in_waiting == 0:
            raise serial.SerialTimeoutException("nbiot串口连接超时")
        _res = ser.readline().decode().strip("\n")
        if res == _res:
            return True
        else:
            return False
    except serial.SerialTimeoutException as e:
        print(e)
        return False
    finally:
        ser.close()

if not connect("AT","OK"):
    raise Exception("nbiot模块异常")

connect("ATE0&W")

time.sleep(0.03)

if not connect("AT+CPIN?","+CPIN: READY"):
    raise Exception("未识别到卡")

if connect("AT+CGATT?","+CGATT: 1"):
    raise Exception("未正常工作")

def send_data(data):
    connect("AT+QICLOSE=0") # 关闭上一次socket连接
    time.sleep(0.03)
    connect(f"AT+QIOPEN=1,0,\"UDP\",\"{server_ip}\",9999,1234,0","+QIOPEN: 0,0")
    encode_data_length = len(data.encode())
    if not connect(f"AT+QISEND=0,{encode_data_length},{data}","SEND OK"):
        raise Exception("发送数据失败")