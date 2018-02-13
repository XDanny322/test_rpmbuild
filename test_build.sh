#!/bin/bash

################################################################################
# Enable debugging (echoing of commands), and halt execution on error
set -x
set -e

################################################################################
# Build variables
RPM_NAME=test_rpm1
version='2017.7.2'
release='1.1'

################################################################################
# Debug / information gathering
# cat /etc/redhat-release
# rpm -q python
# df -h
# whoami

################################################################################
# Prevent Python from including packages found in ~/.local, forcing them to
#   come instead from $WORKSPACE/.local.  This will prevents Jenkins, e.g., from
#   changing its behavior based on packages found in the ~/.local file of the
#   user used for Jenkins builds.
# HOME=/home/vagrant/test_rpmbuild
# echo $HOME

# Special dir
# _topdir = /var/lib/jenkins
# You can overwrite it like so, in the RPMBUILD line: --define "_topdir $HOME"  \
################################################################################
# Build the RPM
rpmbuild \
  --define "name $RPM_NAME"  \
  --define "release $release"  \
  --define "version $version" -ba -vv $HOME/workspace/TestProject/test_rpm.spec
