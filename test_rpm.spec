# http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html

Summary: A very simply rpm package
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Development/Tools
# I think, this is used to ensure files are avaiable as SOURCE
# SOURCE0: %{name}-%{version}.conf
URL: http://test_rpm.company.com/

# I think this is no longer being used.
# BuildRoot:  %{_topdir}/%{name}-%{version}-%{release}-buildroot

%description
%{summary}

# %prep
#  %setup basically turns into a ton of commands:
#  http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
#  %setup -q

# %build
#  Section to does the actua building; IE, make.
#  Empty section.

%configure
echo "~~~~~~~~~~~~~~configure~~~~~~~~~~~~~~~~~~~~~~~~~~~"

%install
echo "~~~~~~~~~~~~~~install~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "Some Debug info"
echo "topdir        = %{_topdir}"       # %{getenv:HOME}/rpmbuild
echo "buildroot     = %{buildroot}"
echo "_rpmdir       = %{_rpmdir}"
echo "_sourcedir    = %{_sourcedir}"
echo "_specdir      = %{_specdir}"
echo "_srcrpmdir    = %{_srcrpmdir}"
echo "_buildrootdir = %{_buildrootdir}"

echo "RPM_BUILD_ROOT= $RPM_BUILD_ROOT"  # /home/vagrant/test_rpmbuild/BUILDROOT/test_rpm-2017.7.2-1.1.x86_64
echo "RPM_BUILD_DIR = $RPM_BUILD_DIR"   # /home/vagrant/test_rpmbuild/BUILD

echo "pwd = `pwd`"

# Starting the install; Gluing the RPM together
install -d -m 0750 $RPM_BUILD_ROOT/tmp/test
cp -vp %{_sourcedir}/test.conf $RPM_BUILD_ROOT/tmp/test/test.conf
cp -vp %{_sourcedir}/test.sh   $RPM_BUILD_ROOT/tmp/test/test.sh

%clean
# rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/tmp/test/test.sh
/tmp/test/test.conf
# %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
# %{_bindir}/*

%changelog
* Mon Jan 29 2018  Danny Lai <XDanny322@gmail.com> 1.0-1
- First Build