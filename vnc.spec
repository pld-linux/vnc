Summary:   Virtual Network Computing
%define name vnc
Name:      %{name}
%define version 3.3.2r3
Version:   %{version}
Release:   2
URL:       http://www.uk.research.att.com/vnc/
Source:    http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_unixsrc.tgz
Source1:   http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_doc.tgz
Patch:     vnc-3.3.2r2-vncserver.patch
Patch1:    vnc-3.3.2r2-ppc.patch
Copyright: GPL
Group:     X11/Applications/Networking
Group:     X11/Aplikacje/Sieciowe
BuildRoot:	/tmp/%{name}-%{version}-root
Summary(pl): Virtual Network Computing -- zdalny desktop

%description
VNC stands for Virtual Network Computing. It is, in essence, a remote display
system which allows you to view a computing 'desktop' environment not only on
the machine where it is running, but from anywhere on the Internet and from a
wide variety of machine architectures.

%description
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu z dowolnej maszynie wyposa¿nej w odpowiedni
serwer.  Dostêpne s± serwery dla Win32, Mac 8.x i X11 a klienty dla Win32,
Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl±darce dzia³aj±cej
po HTTP).

%prep
#%setup -q -n %{name}
%setup -q -n %{name}-%{version} -c
mkdir doc 
cd doc 
gzip -dc %{SOURCE1} | tar -xf - 
cd .. 

%patch -p1
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
install -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -d $RPM_BUILD_ROOT%{_datadir}/vnc/classes
./vncinstall $RPM_BUILD_ROOT/usr/X11R6/bin
install -m644 classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes
strip $RPM_BUILD_ROOT/usr/X11R6/bin/Xvnc
strip $RPM_BUILD_ROOT/usr/X11R6/bin/vncpasswd
strip $RPM_BUILD_ROOT/usr/X11R6/bin/vncviewer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(711,root,root) /usr/X11R6/bin/Xvnc
%attr(711,root,root) /usr/X11R6/bin/vncpasswd
%attr(755,root,root) /usr/X11R6/bin/vncserver
%attr(711,root,root) /usr/X11R6/bin/vncviewer
%{_datadir}/vnc/classes/
%doc doc/
%doc README
