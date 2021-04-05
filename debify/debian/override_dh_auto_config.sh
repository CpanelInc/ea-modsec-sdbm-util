#!/bin/bash

source debian/vars.sh

set -x

sh autogen.sh
./configure \
    --with-apr=$ea_apr_dir \
    --with-apu=$ea_apu_dir

make
