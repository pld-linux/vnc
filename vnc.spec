#
# Conditional build:
# _without_svgalib - without svgalib support
#
%ifnarch %{ix86} alpha
%define _without_svgalib 1
%endif

Summary:	Virtual Network Computing
Summary(es):	Sistema de control remoto
Summary(pl):	Virtual Network Computing - zdalny desktop
Summary(pt_BR):	Sistema de controle remoto
Name:		vnc
Version:	3.3.7
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.realvnc.com/dist/%{name}-%{version}-unixsrc.tar.gz
# Source0-md5:	511ffbc8ed8d9df82e7c67852164728c
Source1:	http://www.realvnc.com/dist/%{name}-%{version}-documentation.tar.gz
# Source1-md5:	0c62c784f1278207fd82693e66ebca40
Source2:	svnc-0.1.tar.bz2
# Source2-md5:	af9a94e1d7795968ce7062fcbe31b84b
Source3:	vncviewer.desktop
Source4:	vnc.png
Patch1:		%{name}-vncserver.patch
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-imake.patch
Patch4:		%{name}-svncviewer.patch
URL:		http://www.realvnc.com/
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
Obsoletes:	tightvnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	vnc-utils
Requires:	xinitrc
Requires:	XFree86-common
Requires:	XFree86-fonts-base
Requires:	XFree86-fonts
Obsoletes:	tightvnc-server

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
Obsoletes:	tightvnc-utils

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

%package svgalib
Summary:	VNC Viewer for svgalib
Summary(pl):	Przegl±darka VNC dla svgaliba
Group:		X11/Applications/Networking

%description svgalib
SVGALIB version of VNC viewer.

%description svgalib -l pl
Klient VNC w wersji dla SVGALIBa.

%prep
%setup -q -n %{name}-%{version}-unixsrc -a1 -a2
%patch1 -p1
%ifarch ppc
%patch2 -p1
%endif
%ifarch sparc sparc64
%patch3 -p1
%endif
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure \
	--with-installed-zlib

%{__make}

cd Xvnc
%{__make} World \
	CDEBUGFLAGS="%{rpmcflags}"
cd -

%if %{!?_without_svgalib:1}%{?_without_svgalib:0}
cd svncviewer
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}"
cd -
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_mandir}/man1}

./vncinstall $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_without_svgalib:1}%{?_without_svgalib:0}
install svncviewer/svncviewer $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_applnkdir}/Network/Misc/vncviewer.desktop
%{_pixmapsdir}/vnc.png

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
%doc %{name}-%{version}-documentation/* README

%if %{!?_without_svgalib:1}%{?_without_svgalib:0}
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svncviewer
%doc svncviewer/README
%endif
