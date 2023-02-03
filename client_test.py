import network.client as client

data = {
    "Motors":
    {
        "speedA":50,
        "directionA":1,
        "speedB":50,
        "directionB":1
    },
    "Servos":
    {
        "pwm1":45,
        "pwm2":135,
    }
}

with client.connect('192.168.2.142:5051') as channels:
    stub=client.get_stub(channels)
    print("Send Command!")
    msg=client.process_data(stub,data)
    print(msg)

