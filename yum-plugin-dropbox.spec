%define pluginhome /usr/lib/yum-plugins
Summary: Allow yum to access repository on Dropbox
Name: yum-plugin-dropbox
Version: 0.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Base
Source: https://github.com/unakatsuo/yum-dropbox/archive/master.tar.gz
URL: https://github.com/unakatsuo/yum-dropbox/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: yum >= 3.2.29
Requires: python-kitchen

%description
This is a yum plugin to access yum repository created on Dropbox. The
authentication is done by OAuth2 so the user is required to get access token
from Dropbox App Console (https://www.dropbox.com/developers/apps)


%prep
%setup -q

%install

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/ $RPM_BUILD_ROOT/%{pluginhome}
install -m 644 dropbox.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
install -m 644 dropbox.py $RPM_BUILD_ROOT/%{pluginhome}
%{__python} -c "import compileall; compileall.compile_dir('$RPM_BUILD_ROOT/%pluginhome', 1)"

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{pluginhome}/dropbox.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/dropbox.conf
