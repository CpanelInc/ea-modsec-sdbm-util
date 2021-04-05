#!/bin/bash

source debian/vars.sh

set -x

rm -rf $DEB_INSTALL_ROOT
make install DESTDIR=$DEB_INSTALL_ROOT
mkdir -p $DEB_INSTALL_ROOT/usr/sbin
mv $DEB_INSTALL_ROOT/usr/local/modsecurity/bin/modsec-sdbm-util $DEB_INSTALL_ROOT/usr/sbin/modsec-sdbm-util

