Summary: NethServer configuration for stephdl repository
Name: nethserver-stephdl
Version: 1.0.4
Release: 2%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no



%description
NethServer configuration for stephdl repository

%prep
%setup

%post

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sat Mar 11 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.4-2
- Added dashboard status

* Fri Feb 24 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.3-1
- Change the email recipient

* Sun Jan 15 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1
- stephdl repo is enabled by default

* Sat Jan 14 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1
- Reinstall stephdl rpm after a restoration

* Sat Sep 24 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-2-ns6
- Adaptation to NS7

* Sun May 2 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1-ns6
- Initial release
