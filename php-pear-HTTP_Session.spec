%define		_class		HTTP
%define		_subclass	Session
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.5.5
Release:	10
Summary:	Object-oriented interface to the session_* family functions
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_Session/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Object-oriented interface to the session_* family functions; it
provides extra features such as database storage for session data
using DB package. It introduces new methods like isNewSession(),
setCookieless(), abandon(), setExpire(), setIdle(), isExpired(),
isIdled() and others.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-8mdv2012.0
+ Revision: 742011
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-7
+ Revision: 679362
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-6mdv2011.0
+ Revision: 613685
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.5-5mdv2010.1
+ Revision: 477898
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.5-4mdv2010.0
+ Revision: 441187
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-3mdv2009.1
+ Revision: 322129
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-2mdv2009.0
+ Revision: 236888
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.5.5-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.5-1mdv2008.0
+ Revision: 15678
- 0.5.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2007.0
+ Revision: 81835
- Import php-pear-HTTP_Session

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdk
- 0.5.2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdk
- 0.5.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdk
- initial Mandriva package (PLD import)

