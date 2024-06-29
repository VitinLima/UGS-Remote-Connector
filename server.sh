#stty -F /dev/ttyUSB0 cs8 -cstopb -parenb 115200
mkfifo p1 p2
nc -l 4444 >p2 <p1 &
python cnc.py <p2 >p1
rm -rf p1 p2
