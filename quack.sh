#!/bin/sh

BIN_FILE_NAME="quack.py"
CONFIG_FILE_NAME="config_parameters.json"

if [ -n "$SNAP_DATA" ]
then
    CONFIG_FILE="$SNAP_DATA/$CONFIG_FILE_NAME"
else
    CONFIG_FILE="$CONFIG_FILE_NAME"
fi

if [ -n "$SNAP" ]
then
    ROOT=$SNAP
else
    ROOT=`pwd`
fi


get_pid() {
    get_pid_result=`ps -ef | grep "[p]ython3 $BIN_FILE_NAME" | awk '{ print $2 }'`
}

start() {
    echo "Starting.."
    get_pid
    pid=$get_pid_result
    if [ -n "$pid" ]
    then
        echo "Quack is already running"
    else
        python3 $BIN_FILE_NAME "start" $CONFIG_FILE
    fi
}
 
stop() {
    echo "Stopping.."
    get_pid
    pid=$get_pid_result
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
    python3 $BIN_FILE_NAME "configure" $CONFIG_FILE
}
 
# Make a choice on the 1st parameter
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
    python3 $BIN_FILE_NAME $@
esac
exit 0
