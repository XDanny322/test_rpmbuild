#!/bin/bash

################################################################################
# Enable debugging (echoing of commands), and halt execution on error
set -x
set -e

################################################################################
# Build variables
SALT_VERSION=${SALT_VERSION:-'2017.7.2'}
BUILD_NUMBER=${BUILD_NUMBER:-'SNAPSHOT'}
RPM_NAME=${RPM_NAME:-'test_rpm'}

################################################################################
# Debug / information gathering
cat /etc/redhat-release
rpm -q python
df -h
whoami

################################################################################
# Prevent Python from including packages found in ~/.local, forcing them to
#   come instead from $WORKSPACE/.local.  This will prevents Jenkins, e.g., from
#   changing its behavior based on packages found in the ~/.local file of the
#   user used for Jenkins builds.
HOME=/home/vagrant/test_rpmbuild
echo $HOME

################################################################################
# Update the salt-minion config file
# sed -i 's/^master:.*$/master: '"$SALT_MASTER"'/' SOURCES/minion.conf

################################################################################
# Build the RPM
pwd
# cd $WORKSPACE
pwd
rpmbuild \
  --define "_topdir $HOME"  \
  --define "name $RPM_NAME"  \
  --define "salt_version $SALT_VERSION" -ba -vv $HOME/test_rpm.spec
