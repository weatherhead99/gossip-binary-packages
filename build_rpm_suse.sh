#!/bin/bash

build gossip.spec --root=`pwd`/buildroot \
      --repo=https://download.opensuse.org/repositories/science/openSUSE_Leap_15.1/ \
      --repo=https://download.opensuse.org/distribution/leap/15.1/repo/oss/ \
      --dist=15.1-x86_64 --cachedir=`pwd`/packagecache
