#
# spec file for package gossip
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gossip
Version:        1.33
Release:        0
Summary:        Generic framework for the simulation of Silicon Photomultipliers
License:        BSD with citation requirement
Group:          Development/Libraries/C and C++
URL:            http://www.kip.uni-heidelberg.de/hep-detektoren/gossip/
Source0:        %{name}-%{version}.tar.gz
Patch0:         suse_build_fix_v%{version}.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  root6-devel
#break dependency issue with libffi
#!BuildIgnore:  ghc-bootstrap
#!BuildIgnore:  musescore-fonts
#!BuildIgnore:  texlive-gnu-freefont-fonts
#needed so that rmkdmod command is available
BuildRequires:  root6

%debug_package

%description
Gossip is a Generic framework for the simulation of Silicon Photomultipliers
The simulation models the response (signal waveform and charge) of a SiPM to an arbitrarylight pulse.  In order to model a specific SiPM, you have to provide a set of basic parametersfor the simulation input.  For a precise simulating of the response, the input parameters haveto be carefully measured!

%package -n libgossip
Summary: Generic framework for the simulation of Silicon Photomultipliers
Group: Development/Libraries/C and C++

%description -n libgossip
Gossip is a Generic framework for the simulation of Silicon Photomultipliers
The simulation models the response (signal waveform and charge) of a SiPM to an arbitrarylight pulse.  In order to model a specific SiPM, you have to provide a set of basic parametersfor the simulation input.  For a precise simulating of the response, the input parameters haveto be carefully measured!

This package contains the gossip shared library and ROOT mapping files

%package devel
Summary: Development and header files for %{name}
Group: Development/Libraries/C and C++
Requires: libgossip = %{version}

%description devel
Development and header files required for developing with gossip (Generic Simulation of Silicon Photomultipliers)


%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/gossip

%files devel
%dir %{_includedir}/gossip
%{_includedir}/gossip/*.h
%dir %{_libdir}/cmake/gossip
%{_libdir}/cmake/gossip/gossipConfig.cmake
%{_libdir}/cmake/gossip/gossipConfigVersion.cmake

%files -n libgossip
%dir %{_libdir}/gossip
%{_libdir}/gossip/libgossip.so
%{_libdir}/gossip/libgossip_rdict.pcm
%{_libdir}/gossip/libgossip.rootmap


%changelog
* Tue May 26 2020 Dan Weatherill <dan.weatherill@cantab.net>
- 1.33
-- package upstream version of gossip based on git tag v1.33
-- add patch to fix build locations on opensuse
