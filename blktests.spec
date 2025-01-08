Name:           blktests
Version:        master
Release:        20250108%{?dist}
Summary:        Linux kernel block layer testing framework

License:        GPL
URL:            https://github.com/osandov/blktests
Source0:        https://github.com/osandov/blktests/archive/master.zip
Packager:       Xiao Liang

BuildRequires:  make gcc
Requires: nvme-cli fio

%define _build_name_fmt        %%{ARCH}/%%{NAME}-%%{VERSION}.%%{ARCH}.rpm

%description
blktests is a test framework for the Linux kernel block layer and storage stack.
It is inspired by the xfstests filesystem testing framework.

%prep
rm -rf /usr/local/blktests
%setup -q -n %{name}-%{version}

%build
#make autotools
#./configure
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
/usr/local/blktests/*
%defattr(-,root,root)
%doc
%changelog
