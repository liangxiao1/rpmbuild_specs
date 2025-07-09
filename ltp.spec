Name:           ltp
Version:        master
Release:        20250709%{?dist}
Summary:        Linux Test Project

License:        GPL
URL:            https://github.com/linux-test-project/ltp
Source0:        https://github.com/linux-test-project/ltp/archive/master.zip
Packager:       Xiao Liang

BuildRequires:  automake,autoconf,sysstat,gcc,unzip,wget,quota,bzip2

%define _build_name_fmt        %%{ARCH}/%%{NAME}-%%{VERSION}.%%{ARCH}.rpm

%description
Linux Test Project is a joint project started by SGI, OSDL and Bull developed
and maintained by IBM, Cisco, Fujitsu, SUSE, Red Hat, Oracle and others. The
project goal is to deliver tests to the open source community that validate
the reliability, robustness, and stability of Linux.

%prep
rm -rf /opt/ltp
%setup -q -n %{name}-%{version}

%build
make autotools
./configure
#./configure --prefix=$RPM_BUILD_ROOT
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
#make DESTDIR=$RPM_BUILD_ROOT install
make install
%make_install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/opt/ltp/*
%defattr(-,root,root)
%doc
%changelog
