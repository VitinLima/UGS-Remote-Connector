#programdir="/home/vitinho/UGS-Remote-Connector"
#echo ${USER} > $programdir/userinfo.txt
mkfifo $programdir/p1 $programdir/p2
#python $programdir/cnc.py <$programdir/p2 >$programdir/pyout.txt 2>&1 &
nc -l -k 4444 >$programdir/p2 <$programdir/p1 &
NCID=$!
python $programdir/cnc.py <$programdir/p2 >$programdir/p1
# 2>&1
rm -rf $programdir/p1 $programdir/p2
kill $NCID
