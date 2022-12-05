#! /usr/bin/env bash

/au/control/alcorInit.sh 666 /tmp

#/au/readout/bin/readout --connection /au/etc/connection2.xml --fifo 1 --output /home/eic/DATA/READOUT/test --monitor-period 900000 --mode 11 --timeout 1000000
/au/readout/bin/readout --connection /au/etc/connection2.xml --fifo 1 --output /home/eic/DATA/READOUT/test --monitor-period 900000 --mode 3

/au/readout/bin/decoder --input /home/eic/DATA/READOUT/test.fifo_0.dat --output /home/eic/DATA/READOUT/test.fifo_0.decoded  --verbose

root -b -q -l "/home/eic/alcor/alcor-utils/readout/macros/makeTree.C(\"/home/eic/DATA/READOUT/test.fifo_0.decoded\", \"/home/eic/DATA/READOUT/test.fifo_0.root\")"
