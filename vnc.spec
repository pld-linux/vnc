Summary:   	Virtual Network Computing
Summary(pl):    Virtual Network Computing -- zdalny desktop
Name:		vnc
Version:	3.3.2r3
Release:	2
Copyright:      GPL
Group:          X11/Applications/Networking
Group(pl):      X11/Aplikacje/Sieciowe
Source0:	http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_unixsrc.tgz
Source1:	http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_doc.tgz
Patch0:		vnc-3.3.2r2-vncserver.patch
Patch1:		vnc-3.3.2r2-ppc.patch
URL:            http://www.uk.research.att.com/vnc/
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
VNC stands for Virtual Network Computing. It is, in essence, a remote display
system which allows you to view a computing 'desktop' environment not only on
the machine where it is running, but from anywhere on the Internet and from a
wide variety of machine architectures.

%description -l pl
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu z dowolnej maszynie wyposa¿nej w odpowiedni
serwer.  Dostêpne s± serwery dla Win32, Mac 8.x i X11 a klienty dla Win32,
Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl±darce dzia³aj±cej
po HTTP).

%prep
%setup -q -c
mkdir doc 
cd doc 
gzip -dc %{SOURCE1} | tar -xf - 
cd .. 

%patch0 -p1
%ifarch ppc
%patch1 -p1
%endif

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" World
cd Xvnc
make CDEBUGFLAGS="$RPM_OPT_FLAGS" World

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes}

./vncinstall $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

strip $RPM_BUILD_ROOT%{_bindir}/{Xvnc,vncpasswd,vncviewer}

gzip -9nf README doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/vnc
