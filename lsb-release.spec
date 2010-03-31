Summary: Linux Standard Base tools
Name: lsb-release
Version: 2.0
Release: %mkrel 24
License: GPL
Source: lsb-release-%{version}.tar.bz2
Group: System/Base
URL:  http://www.freestandards.org/en/LSB
BuildRoot: %{_tmppath}/%{name}-root
ExclusiveArch: %{ix86} x86_64 ppc

%define lsbver 4.0
%define arch_name ia32 

%ifarch x86_64
%define arch_name amd64 
%endif
%ifarch %{ppc}
%define arch_name ppc 
%endif

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

%setup

%build
rm -rf $RPM_BUILD_ROOT
make

%install
make prefix=%buildroot mandir=%buildroot/%{_mandir} install 
mkdir -p %buildroot/%{_sysconfdir}/%{name}.d
mkdir -p %buildroot/%{_sysconfdir}
cat > %buildroot/%{_sysconfdir}/lsb-release << EOF
LSB_VERSION=lsb-%{lsbver}-%arch_name:lsb-%{lsbver}-noarch
DISTRIB_ID=MandrivaLinux
DISTRIB_RELEASE=2010.1
DISTRIB_CODENAME=john_stringfellow
DISTRIB_DESCRIPTION="%{distribution} 2010.1"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/bin/lsb_release
%{_mandir}/man1/lsb_release.1*
%config(noreplace) %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}.d
