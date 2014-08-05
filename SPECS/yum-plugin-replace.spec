
Name: yum-plugin-replace        
Version:    0.2.7
Release:    1.ius%{?dist}
Summary:    Package Replacement Plugin for Yum

Group:      System Environment/Base     
License:    GPL
URL:        https://github.com/iuscommunity/yum-plugin-replace 
Source0:     https://codeload.github.com/iuscommunity/%{name}/tar.gz/%{version}
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

Requires:   yum  

%description
This plugin enables the ability to replace an installed package, with another
package that provides the same thing.  It was developed specifically for the
IUS Community Project whose packages have alternative names as to not
automatically upgrade stock packages.  They also do not Obsolete the packages
they provide, therefore making upgrading a little bit more tedious.  For
example upgrading 'mysql' to 'mysql50' or 'mysql51' requires first
uninstalling 'mysql' and then installing the alternate package name. 

%prep
%setup -q


%build
# pass

%install
rm -rf %{buildroot}
%{__mkdir} -p   %{buildroot}%{_sysconfdir}/yum/pluginconf.d/ \
                %{buildroot}%{_prefix}/lib/yum-plugins/

%{__install} -m 0644 ./etc/yum/pluginconf.d/replace.conf \
    %{buildroot}%{_sysconfdir}/yum/pluginconf.d/
%{__install} -m 0644 ./lib/yum-plugins/replace.py \
    %{buildroot}%{_prefix}/lib/yum-plugins/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README LICENSE ChangeLog
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/replace.conf
%{_prefix}/lib/yum-plugins/replace.py*



%changelog
* Tue Aug 05 2014 Ben Harper <ben.harper@rackspace.com> - 0.2.7-1.ius
- pulling in https://github.com/iuscommunity/yum-plugin-replace/pull/6

* Tue Jun 25 2013 Ben Harper <ben.harper@rackspace.com> - 0.2.6-1.ius
- pulling in https://github.com/iuscommunity/yum-plugin-replace/pull/4
- pulling in https://github.com/iuscommunity/yum-plugin-replace/pull/5

* Mon Sep 24 2012 jeffrey.ness@rackspace.com - 0.2.5-1.ius
- Attempt to auto resolve when multiple provides are found
  https://github.com/iuscommunity/yum-plugin-replace/issues/2

* Thu Jul 28 2011 wdierkes@rackspace.com - 0.2.4-3
- Rebuild for EL6

* Wed Aug 11 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.2.4-2
- BuildArch: noarch

* Tue Aug 10 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.2.4-1
- Latest sources

* Fri Aug 06 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.2.2-1
- Latest sources

* Fri Jul 30 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.2-1
- Latest sources

* Tue Jul 13 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.1-1
- Initial spec build.

