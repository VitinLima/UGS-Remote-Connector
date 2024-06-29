mkfifo p1 p2
python cnc.py <p2 >p1 &
nc -l -k 4444 >p2 <p1
rm -rf p1 p2
