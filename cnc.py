import time
import serial
import sys
import threading

class InputHandler(threading.Thread):
  def __init__(self, ser):
    super().__init__()
    self.ser = ser
  
  def run(self):
    self.running = True
    incomming = ''
    while self.running:
      while self.ser.in_waiting>0:
        c = self.ser.read().decode()
        # with open("cncout.txt", 'w') as f:
        #   f.write(c)
        print(c, end='', flush=True)
  
  # def readline(self):
  #   self.in_buffer -= 1
  #   return self.lines.pop(0)

if __name__=="__main__":
  flag = True
  with serial.Serial('/dev/ttyACM0', 115200) as ser:
#   with serial.Serial('/dev/ttyUSB0', 115200) as ser:
    input_thread = InputHandler(ser)
    input_thread.daemon = True
    input_thread.start()
    with open("log.txt", 'w') as f:
      while flag:
        line = sys.stdin.readline()
        if line=="^C\n":
          flag = False
          input_thread.running = False
        else:
          ser.write(bytes(line,'utf-8'))
          f.write(bytes(line,'utf-8'))
    input_thread.running = False
    input_thread.join()
