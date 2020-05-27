#!/bin/bash

build ~/rpmbuild/SPECS/gossip.spec --root=`pwd`/buildroot --repo=https://download.opensuse.org/distribution/leap/15.1/repo/oss/ --repo=https://download.opensuse.org/repositories/science/openSUSE_Leap_15.1/  --dist=15.1 --cachedir=`pwd`/packagecache
