#!/bin/sh

CONFIG_FILE="$SNAP_DATA/config_parameters.json"
ROOT=$SNAP

start() {
    echo "Starting.."
    pid=`ps -ef | grep '[p]ython3 quack.py' | awk '{ print $2 }'`
    if [ -n "$pid" ]
    then
        echo "Quack is already running"
    else
        python3 $quack.py start $CONFIG_FILE
    fi
}
 
stop() {
    echo "Stopping.."
    pid=`ps -ef | grep '[p]ython3 quack.py' | awk '{ print $2 }'`
    if [ -n "$pid" ]
    then
        echo $pid
        kill $pid
        sleep 2
        echo "Quack has stopped"
    else
        echo "Quack is not running"
    fi
}

configure() {
    python3 quack.py configure $CONFIG_FILE
}
 
case "$1" in
  start)
    start
    ;;
  stop)
    stop   
    ;;
  restart)
    stop
    start
    ;;
  configure)
    configure
    ;;
  *)
    python3 quack.py $1
esac
exit 0
