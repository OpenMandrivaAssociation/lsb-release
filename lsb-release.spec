%define debug_package %{nil}

Summary:	Linux Standard Base tools
Name:		lsb-release
Version:	3.2
Release:	20
License:	GPL
Group:		System/Base
URL:		https://github.com/thkukuk/lsb-release_os-release
Source0:	https://github.com/thkukuk/lsb-release_os-release/archive/refs/tags/%{name}_os-release-%{version}.tar.gz
Requires(pre):	filesystem
BuildRequires:	distro-release
BuildArch:	noarch

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
%autosetup -p1 -n %{name}_os-release-%{version}

%build
make

%install
%make_install INSTALL_ROOT=%{buildroot}%{_prefix}

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}.d
mkdir -p %{buildroot}/%{_sysconfdir}
# set codename accordingly to https://wiki.openmandriva.org/en/policies/codename
cat > %{buildroot}/%{_sysconfdir}/lsb-release << EOF
LSB_VERSION=
DISTRIB_ID="%{distribution}"
DISTRIB_RELEASE=%{product_version}
DISTRIB_CODENAME=ROME
DISTRIB_DESCRIPTION="%{distribution} %{product_version}"
EOF

%files
%doc README
%{_bindir}/lsb*release
%doc %{_mandir}/man1/lsb*.1*
%config(noreplace) %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}.d
