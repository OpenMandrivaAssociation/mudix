%define	name	mudix
%define	version	4.3
%define release  12

Name:		%{name} 
Summary:	Console mud client
Version:	%{version} 
Release:	%{release} 
Source0:	http://dw.nl.eu.org/mudix/%{name}-%{version}.tar.bz2
URL:		https://dw.nl.eu.org/mudix.html
Group:		Games/Other
License:	BSD-like
BuildRequires:  ncurses-devel


%description
Mudix is a console mud client that supports ANSI colours.
Some of the features are aliases, timers and triggers.

%prep
%setup -q

%build
%configure
%make O_FLAGS="%{optflags}"

%install
install -m755 mudix -D %{buildroot}%{_gamesbindir}/mudix

%clean 

%files 
%doc README
%{_gamesbindir}/mudix



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 4.3-10mdv2011.0
+ Revision: 620416
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 4.3-9mdv2010.0
+ Revision: 430116
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.3-8mdv2009.0
+ Revision: 253075
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 4.3-6mdv2008.1
+ Revision: 140966
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3-6mdv2008.0
+ Revision: 89968
- rebuild

* Sat Aug 18 2007 Eskild Hustvedt <eskild@mandriva.org> 4.3-5mdv2008.0
+ Revision: 66399
- Rebuild


* Mon Apr 10 2006 Michael Scherer <misc@mandriva.org> 4.3-4mdk
- Rebuild
- use mkrel

* Wed Feb 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.3-3mdk
- compile with $RPM_OPT_FLAGS
- move binary to %%{_gamesbindir}
- from Eskild Hustvedt <zerodogg@skolelinux.no> :
	o Spec cleanup

* Thu Sep 02 2004 Michael Scherer <misc@mandrake.org> 4.3-2mdk 
- BuildRequires

* Sat Jul 03 2004 Eskild Hustvedt <eskild@mandrakehelp.com> 4.3-1mdk
- Initial Mandrakelinux package

