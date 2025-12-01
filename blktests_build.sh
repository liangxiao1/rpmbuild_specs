set -x
rm -rf /root/rpmbuild_specs
yum install -y rpm-build rpmdevtools make gcc gcc-c++ wget
rm -rf /root/rpmbuild/*
rpmdev-setuptree
cd /root
mkdir rpms
git clone https://github.com/liangxiao1/rpmbuild_specs.git
spectool -g -R /root/rpmbuild_specs/blktests.spec
rpmbuild --undefine dist --define "debug_package %{nil}"  -ba /root/rpmbuild_specs/blktests.spec
find /root/rpmbuild/RPMS -name "*.rpm" -exec mv {} rpms \;