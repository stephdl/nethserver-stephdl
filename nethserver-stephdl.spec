Summary: NethServer configuration for stephdl repository
Name: nethserver-stephdl
Version: 1.1.4
Release: 1%{?dist}
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
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
chmod +x %{buildroot}/usr/libexec/nethserver/api/%{name}/*

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%attr(0755,root,root) %{_sysconfdir}/cron.daily/check4StephdlUpdates
%config(noreplace) /etc/yum.repos.d/stephdl-roundcubemail.repo
%config(noreplace) /etc/yum.repos.d/stephdl-dolibarr.repo
%config(noreplace) /etc/yum.repos.d/stephdl.repo

%changelog
* Thu Jan 14 2021 stephane de labrusse <stephdl@de-labrusse.fr> - 1.1.4-1
- Enhance donation in cockpit application
- Email to administrator

* Fri Nov 06 2020 stephane de labrusse <stephdl@de-labrusse.fr> - 1.1.3-1
- Display stephdl repo inside the the cockpit application list

* Mon Sep 28 2020 stephane de labrusse <stephdl@de-labrusse.fr> - 1.1.2-1
- Include eorepo inside configuration backup

* Tue Jun 20 2020 stephane de labrusse <stephdl@de-labrusse.fr> - 1.1.1-1
- Enable this repository for subscription

* Sun May 03 2020 stephane de labrusse <stephdl@de-labrusse.fr> - 1.1.0-1
- Emphasys Donation
- Add explanations how to update dolibarr and roundcubemail

* Wed Apr 29 2020 stephane de labrusse <stephdl@de-labrusse.fr> - 1.0.12-1
- Warns about updates for dolibarr and roundcubemail
 
* Fri Apr 17 2020 stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.11-1
- Yum repository conf are no replace

* Tue Apr 14 2020 stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.10-1
- enable stephdl-dolibarr repository

* Wed Apr 8 2020 stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.9-1
- enable stephdl-roundcubemail repository

* Wed Jun 5 2019 Stephane de Labrusse  <stephdl@de-labrusse.fr> - 1.0.8-1
- Enable stephdl repo with  software-repos-save

* Tue Aug 21 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.7-1
- give permisions execution to check4StephdlUpdates

* Sat Sep 09 2017 Stephane de LAbrusse <stephdl@de-labrusse.fr> - 1.0.6-1
- don't forget to email root on update

* Mon Sep 04 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.5-1
- donation asked by email

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.4-3
- GPL license

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
