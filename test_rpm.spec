# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

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

%prep
# Don't use the setup macro anymore, replace it with typed-out commands
# https://serverfault.com/a/805721
# %setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/tmp/%{name}.conf
/tmp/%{name}
# %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
# %{_bindir}/*

%changelog
* Mon Jan 29 2018  Danny Lai <XDanny322@gmail.com> 1.0-1
- First Build