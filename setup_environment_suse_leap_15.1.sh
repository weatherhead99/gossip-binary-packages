#!/bin/bash

#add science repo
zypper -n addrepo https://download.opensuse.org/repositories/science/openSUSE_Leap_15.1/ science
zypper -n refresh

#install ROOT6 devel environment
zypper -n in root6 root6-devel cmake gcc-c++ rpmdevtools rpm-build


