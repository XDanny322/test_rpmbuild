# http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html

# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing

# Commenting out for now, not sure what it goes
# %define        __spec_install_post %{nil}
# %define          debug_package %{nil}
# %define        __os_install_post %{_dbpath}/brp-compress

Summary: A very rpm package
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL+
Group: Development/Tools
SOURCE0 : %{name}-%{version}.conf
URL: http://testrpm.company.com/

BuildRoot:  %{_topdir}/%{name}-%{version}-%{release}-buildroot

%description
%{summary}

# Used to PrePrep the build
# %prep
# # This will auto cd into the BUILD dir
# echo "~~~~~~~~~~~~~~prep~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# echo "RPM_BUILD_DIR = $RPM_BUILD_DIR" # /home/vagrant/test_rpmbuild/BUILD
# rm -rf $RPM_BUILD_DIR/

# %setup basically turns into a ton of commands:
# http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
# %setup -q


# Section to does the actua building
# %build
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# echo "Preping -build-"
# Empty section.

%configure
echo "~~~~~~~~~~~~~~configure~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Preping -configure-"

%install
echo "~~~~~~~~~~~~~~install~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Preping -install-"
echo "buildroot= %{buildroot}"
echo "RPM_BUILD_ROOT= $RPM_BUILD_ROOT"  # /home/vagrant/test_rpmbuild/BUILDROOT/test_rpm1-2017.7.2-1.1.x86_64
echo "RPM_BUILD_DIR = $RPM_BUILD_DIR"   # /home/vagrant/test_rpmbuild/BUILD
echo "pwd = `pwd`"

# Moving the stuff into dir ready for packaging
# touch $RPM_BUILD_DIR/test.txt
# rm -rf %{buildroot}
# mkdir -p  %{buildroot}

# in builddir
# cp -a * %{buildroot}


%clean
# rm -rf $RPM_BUILD_ROOT

%files
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
%defattr(-,root,root,-)
/tmp/%{name}.conf
/tmp/%{name}
# %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
# %{_bindir}/*

%changelog
* Mon Jan 29 2018  Danny Lai <XDanny322@gmail.com> 1.0-1
- First Build


 # BUILD
 # BUILDROOT
 # RPMS
 # SRPMS
 # SOURCES
 # SPECS   -> Spec file
