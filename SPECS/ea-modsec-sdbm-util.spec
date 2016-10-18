# Defining the package namespace
%global ns_name ea
%global upstream_name modsec-sdbm-util

%define        debug_package %{nil}
%define        release_prefix 1

Name:          %{ns_name}-%{upstream_name}
Version:       0.01
Release:       %{release_prefix}%{?dist}.cpanel
License:       Apache 2.0
Vendor:        cPanel, Inc.
Summary:       EasyApache4 RPM package for modsec-sdbm-util
Url:           https://github.com/SpiderLabs/modsec-sdbm-util
Group:         Development/Tools
Source:        %{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ea-apr-devel >= 1.5.0, ea-apr-util-devel >= 1.2.0
Requires:      ea-apr >= 1.5.0, mod_security2

%description
Utility to manipulate SDBM files used by ModSecurity. With that utility it is
possible to shrink SDBM databases. It is also possible to list the SDBM contents
with filters such as: expired or invalid items only.

%prep
%setup -q

%build
sh autogen.sh
%configure --with-apr=%{ea_apr_dir} --with-apu=%{ea_apu_dir}
%{__make} %{_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir %{buildroot}/usr/sbin
mv %{buildroot}/usr/bin/modsec-sdbm-util %{buildroot}/usr/sbin/modsec-sdbm-util

%clean
rm -rf %{buildroot}

%files
%attr(0750,root,root) /usr/sbin/modsec-sdbm-util

%changelog
* Tue Oct 11 2016 Brett Estrade <brett@cpanel.net> 0.01-1
- First Build
