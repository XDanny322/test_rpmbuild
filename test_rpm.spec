# http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html

Summary: A very simply rpm package
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Development/Tools
# I think, this is used to ensure files are avaiable as SOURCE
# SOURCE0: %{name}-%{version}.conf
URL: http://testrpm.company.com/

BuildRoot:  %{_topdir}/%{name}-%{version}-%{release}-buildroot

%description
%{summary}

# As part of the bild, rpmbuild will auto cd into the RPM_BUILD_ROOT
# and clean up

# %prep
# %setup basically turns into a ton of commands:
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
# %setup -q

# %build
# Section to does the actua building; IE, make.
# Empty section.

%configure
echo "~~~~~~~~~~~~~~configure~~~~~~~~~~~~~~~~~~~~~~~~~~~"

%install
echo "~~~~~~~~~~~~~~install~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "Some Debug info"
echo "buildroot= %{buildroot}"
echo "RPM_BUILD_ROOT= $RPM_BUILD_ROOT"  # /home/vagrant/test_rpmbuild/BUILDROOT/test_rpm1-2017.7.2-1.1.x86_64
echo "RPM_BUILD_DIR = $RPM_BUILD_DIR"   # /home/vagrant/test_rpmbuild/BUILD
echo "pwd = `pwd`"

install -d -m 0750 $RPM_BUILD_ROOT/tmp/test
cp -vp /home/vagrant/test_rpmbuild/SOURCES/test.conf $RPM_BUILD_ROOT/tmp/test/test.conf
cp -vp /home/vagrant/test_rpmbuild/SOURCES/test.sh   $RPM_BUILD_ROOT/tmp/test/test.sh

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
