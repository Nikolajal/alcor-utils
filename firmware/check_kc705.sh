#! /usr/bin/env bash

source /tools/Xilinx/Vivado_Lab/2021.2/.settings64-Vivado_Lab.sh
source /home/eic/alcor/alcor-utils/etc/env.sh

FW="new"
FW="dev"
TARGET=210203A62F62A
TARGET=210203AB8FBFA
TARGET=210203B1C64EA
if [ ! -x $KC705_TARGET ]; then
    TARGET=$KC705_TARGET
fi

ping -c1 10.0.8.15 && exit 0

/home/eic/alcor/alcor-utils/firmware/program.sh $FW $TARGET true &> /tmp/firmware_program.log
/home/eic/alcor/alcor-utils/control/alcorInit.sh 666 /tmp &> /dev/null
