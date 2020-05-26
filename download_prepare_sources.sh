#!/bin/bash

VERSION=1.33

if [ ! -d "~/rpmbuild" ]; then
   echo "need to setup rpmbuild tree"
   rpmdev-setuptree
fi


echo "cloning gossip and making source archive..."
git clone https://github.com/kip-hep-detectors/gossip
cd gossip
git archive v${VERSION} --format=tar --prefix=gossip-${VERSION}/ > ../gossip-${VERSION}.tar.gz
cd ..

echo "linking source and specfiles to rpmbuild tree..."
ln -s `pwd`/gossip-${VERSION}.tar.gz ~/rpmbuild/SOURCES/
ln -s `pwd`/suse_build_fix.patch ~/rpmbuild/SOURCES/
ln -s `pwd`/gossip.spec ~/rpmbuild/SPECS/
