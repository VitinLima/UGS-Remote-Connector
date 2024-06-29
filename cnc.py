import time
import serial
import sys
import threading

class InputHandler(threading.Thread):
  def run(self):
    self.running = True
    self.lines = []
    self.in_buffer = 0
    while self.running:
      self.lines.append(sys.stdin.readline())
      self.in_buffer += 1
  
  def readline(self):
    self.in_buffer -= 1
    return self.lines.pop(0)


if __name__=="__main__":
  #with serial.Serial('/dev/ttyACM0', 115200) as ser:
  with serial.Serial('/dev/ttyUSB0', 115200) as ser:
    flag = True
    input_thread = InputHandler()
    input_thread.daemon = True
    input_thread.start()
    while flag:
      while ser.in_waiting>0:
        print(ser.read.decode(), end='', flush=True)
      while input_handler.in_buffer:
        line = input_thread.readline()
        if line=="^C\n":
          flag = False
          input_thread.running = False
        else:
          ser.write(bytes(line,'utf-8'))
