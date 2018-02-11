#!/bin/bash

################################################################################
# Enable debugging (echoing of commands), and halt execution on error
set -x
set -e

################################################################################
# Build variables
SALT_VERSION=${SALT_VERSION:-'2017.7.2'}
AUTOMATION_VERSION=${AUTOMATION_VERSION:-'12'}
FULL_VERSION="$SALT_VERSION.$AUTOMATION_VERSION"
BUILD_NUMBER=${BUILD_NUMBER:-'SNAPSHOT'}
SALT_MASTER=${SALT_MASTER:-'localhost'}
RPM_NAME=${RPM_NAME:-'fds-auto-salt-minion'}
PIP_VERSION=${PIP_VERSION:-'9.0.1'}

################################################################################
# Debug / information gathering
cat /etc/redhat-release
rpm -q python
df -h
whoami
echo $WORKSPACE

################################################################################
# Prevent Python from including packages found in ~/.local, forcing them to
#   come instead from $WORKSPACE/.local.  This will prevents Jenkins, e.g., from
#   changing its behavior based on packages found in the ~/.local file of the
#   user used for Jenkins builds.
HOME=$WORKSPACE
echo $HOME

################################################################################
# Update the salt-minion config file
# sed -i 's/^master:.*$/master: '"$SALT_MASTER"'/' SOURCES/minion.conf

################################################################################
# Build the RPM
pwd
cd $WORKSPACE
pwd
rpmbuild \
  --define "_topdir $WORKSPACE"  \
  --define "name $RPM_NAME"  \
  --define "salt_version $SALT_VERSION"  \
  --define "version $FULL_VERSION"  \
  --define "release $BUILD_NUMBER%{?dist}"  \
  --define "salt_minion_config minion.conf"  \
  --define "salt_minion_service salt-minion.service.systemd"  \
  --define "logrotate_config salt.logrotate"  \
  --define "pip_version $PIP_VERSION" -ba -vv test_rpm.spec
