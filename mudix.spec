%define	name	mudix
%define	version	4.3
%define	release %mkrel 8

Name:		%{name} 
Summary:	Mudix console mud client
Version:	%{version} 
Release:	%{release} 
Source0:	http://dw.nl.eu.org/mudix/%{name}-%{version}.tar.bz2
URL:		http://dw.nl.eu.org/mudix.html
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	BSD-like
BuildRequires:  ncurses-devel


%description
Mudix is a console mud client that supports ANSI colours.
Some of the features are aliases, timers and triggers.

%prep
%setup -q

%build
%configure
%make O_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 mudix -D $RPM_BUILD_ROOT%{_gamesbindir}/mudix

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README
%{_gamesbindir}/mudix

