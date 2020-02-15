Summary: Linux Standard Base tools
Name: lsb-release
Version: 2.0
Release: 53
License: GPL
Source: lsb-release-%{version}.tar.bz2
Patch0: lsb-release-%{version}-no-support.patch
Group: System/Base
URL: http://bzr.linuxfoundation.org/loggerhead/lsb/devel/si/files/head:/lsb_release/ 

%define debug_package %{nil}

%description
LSB version query program

This program forms part of the required functionality of
the LSB (Linux Standard Base) specification.

The program queries the installed state of the distribution
to display certain properties such as the version of the
LSB against which the distribution claims compliance as 
well. It can also attempt to display the name and release
of the distribution along with an identifier of who produces
the distribution.

%prep

%setup -q
%patch0 -p1 -b .no-support

%build
make

%install
make prefix=%{buildroot} mandir=%{buildroot}/%{_mandir} install 
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}.d
mkdir -p %{buildroot}/%{_sysconfdir}
# set codename accordingly to https://wiki.openmandriva.org/en/Codename
cat > %{buildroot}/%{_sysconfdir}/lsb-release << EOF
LSB_VERSION=
DISTRIB_ID=OpenMandrivaLinux
DISTRIB_RELEASE=%{product_version}
DISTRIB_CODENAME=Argon
DISTRIB_DESCRIPTION="%{distribution} %{product_version}"
EOF

mkdir -p %{buildroot}/usr/bin
pushd %{buildroot}/usr/bin
ln -sf /bin/lsb_release lsb_release
popd


%files
%doc README
/bin/lsb_release
%_bindir/lsb_release
%{_mandir}/man1/lsb_release.1*
%config(noreplace) %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}.d

