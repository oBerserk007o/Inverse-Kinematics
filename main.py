import socket
import struct
import numpy as np

# receive string of dict -> convert string of dict to actual dict -> read and process values ->
# write results to json file -> read json to string -> send string as bytes


# https://stackoverflow.com/questions/57080210/how-to-make-c-sharp-in-unity-communicate-with-python
# Thank you to user 'abujaman' for this code
def sending_and_receiving():
    s = socket.socket()
    socket.setdefaulttimeout(None)
    print('socket created ')
    port = 60000
    s.bind(('127.0.0.1', port))
    s.listen(30) #listening for connection for 30 sec?
    print('socket listening ... ')
    while True:
        try:
            c, addr = s.accept() #when port connected
            bytes_received = c.recv(4000) #received bytes
            array_received = np.frombuffer(bytes_received, dtype=np.float32) #converting into float array

            output = [array_received[0] + 1]
            print(array_received)

            bytes_to_send = struct.pack('%sf' % len(output), *output) #converting float to byte
            c.sendall(bytes_to_send) #sending back
            c.close()
        except Exception as e:
            print("error")
            c.sendall(bytearray([]))
            c.close()
            break


sending_and_receiving()
