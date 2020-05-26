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
Version:        1.31
Release:        0
Summary:        Generic framework for the simulation of Silicon Photomultipliers
License:        BSD with citation requirement
URL:            www.kip.uni-heidelberg.de/hep-detektoren/gossip/
Source0:        %{name}-%{version}.tar.gz
Patch0:         suse_build_fix_v%{version}.patch
BuildRequires:  gcc-c++

%description


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

%changelog
