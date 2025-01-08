set -x
rm -rf /root/rpmbuild_specs
yum install -y rpm-build rpmdevtools wget autoconf automake sysstat gcc quota git make
rm -rf /root/rpmbuild/*
rpmdev-setuptree
cd /root
mkdir rpms
cd /root/rpmbuild/SOURCES
wget https://github.com/linux-test-project/ltp/archive/master.zip
cd /root
git clone https://github.com/liangxiao1/rpmbuild_specs.git
rpmbuild --undefine dist --define "debug_package %{nil}"  -ba /root/rpmbuild_specs/ltp.spec
find /root/rpmbuild/RPMS -name "*.rpm" -exec mv {} rpms \;