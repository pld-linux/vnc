Summary:	Virtual Network Computing
Summary(es):	Sistema de control remoto
Summary(pl):	Virtual Network Computing -- zdalny desktop
Summary(pt_BR):	Sistema de controle remoto
Name:		vnc
Version:	3.3.3r2
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_unixsrc.tgz
Source1:	http://www.uk.research.att.com/vnc/dist/%{name}-latest_doc.tgz
Source2:	vncviewer.1
Source3:	%{name}-Xvnc.1
Source4:	vncserver.1
Source5:	vncconnect.1
Source6:	vncpasswd.1
Source7:	vncviewer.desktop
Patch0:		http://www.ce.cctpu.edu.ru/vnc/preview/%{name}-%{version}-unix-tight-1.1p4.patch.gz
Patch1:		%{name}-vncserver.patch
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-ComplexProgramTargetNoMan.patch
Patch4:		%{name}-corre.patch
Patch5:		%{name}-typo.patch
URL:		http://www.uk.research.att.com/vnc/
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_noautocompressdoc	*.GIF

%description
VNC stands for Virtual Network Computing. It is, in essence, a remote
display system which allows you to view a computing 'desktop'
environment not only on the machine where it is running, but from
anywhere on the Internet and from a wide variety of machine
architectures.

This package contains VNC viewer.

%description -l es
Sistema de control remoto.

%description -l pl
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu na dowolnej maszynie wyposa¿onej w odpowiedni
serwer. Dostêpne s± serwery dla Win32, Mac 8.x i X11, a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl±darce
dzia³aj±cej po HTTP).

Ten pakiet zawiera program wy¶wietlaj±cy ekran VNC (vncviewer).

%description -l pt_BR
VNC (Virtual Network Computing) ' um sistema de controle remoto que
permite visualizar um ambiente desktop nÇo somente da m quina onde o
VNC est  rodando, mas de qualquer lugar da Internet e de uma variedade
de arquiteturas. O VNC ' diferente de um servidor X em v rios
aspectos: nÇo salva nenhum estado no visualizador VNC, ' pequeno e
simples, ' de fato independente de plataforma, e um desktop pode ser
visto e usado por diversos visualizadores ao mesmo tempo.

%package server
Summary:	VNC X server
Summary(es):	Sistema de control remoto
Summary(pl):	X serwer VNC
Summary(pt_BR):	Sistema de controle remoto
Group:		X11/Applications/Networking
Requires:	XFree86-common

%description server
VNC stands for Virtual Network Computing. It is, in essence, a remote
display system which allows you to view a computing 'desktop'
environment not only on the machine where it is running, but from
anywhere on the Internet and from a wide variety of machine
architectures.

This package contains VNC X server (Xvnc).

%description server -l es
Sistema de control remoto.

%description server -l pl
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu na dowolnej maszynie wyposa¿onej w odpowiedni
serwer. Dostêpne s± serwery dla Win32, Mac 8.x i X11, a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl±darce
dzia³aj±cej po HTTP).

Ten pakiet zawiera X serwer VNC (Xvnc).

%description server -l pt_BR
VNC (Virtual Network Computing) ' um sistema de controle remoto que
permite visualizar um ambiente desktop nÇo somente da m quina onde o
VNC est  rodando, mas de qualquer lugar da Internet e de uma variedade
de arquiteturas. O VNC ' diferente de um servidor X em v rios
aspectos: nÇo salva nenhum estado no visualizador VNC, ' pequeno e
simples, ' de fato independente de plataforma, e um desktop pode ser
visto e usado por diversos visualizadores ao mesmo tempo.

%package utils
Summary:	Additional utilities for VNC
Summary(pl):	Dodatkowe narzêdzia do VNC
Group:		X11/Applications/Networking

%description utils
This package contains additional VNC utilities: vncconnect and
vncpasswd. vncconnect tells Xvnc server to connect to a listening VNC
viewer. vncpasswd generates password file (both on server and
viewer side).

%description utils -l pl
Ten pakiet zawiera dodatkowe narzêdzia VNC: vncconnect i vncpasswd.
vncconnect s³u¿y do po³±czenia serwera Xvnc z nas³uchuj±cym
vncviewerem. vncpasswd s³u¿y to tworzenia pliku z has³em (zarówno po
stronie serwera, jak i przegl±darki).

%package doc
Summary:	VNC documentation
Summary(pl):	Dokumentacja do VNC
Group:		Documentation

%description doc
This package contains documentation for VNC protocol, utilities etc.

%description doc -l pl
Ten pakiet zawiera dokumentacjê do VNC (protoko³u, programów itp.).

%prep
%setup -q -n %{name}_unixsrc -a1
%patch0 -p1
%patch1 -p1
%ifarch ppc
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -rf Xvnc/lib/zlib

xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}" ZLIB_LIB="-lz" World
%{__make} World -C Xvnc \
	CDEBUGFLAGS="%{rpmcflags}" ZLIBDIR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_applnkdir}/Network}

./vncinstall $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

install %{SOURCE2} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/Xvnc.1

install %{SOURCE7} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_applnkdir}/Network/vncviewer.desktop

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvnc
%attr(755,root,root) %{_bindir}/vncserver
%{_datadir}/vnc
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncserver.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconnect
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconnect.1*
%{_mandir}/man1/vncpasswd.1*

%files doc
%defattr(644,root,root,755)
%doc vnc_docs/*.{gif,jpg,html,htm,pdf,css,GIF} README
