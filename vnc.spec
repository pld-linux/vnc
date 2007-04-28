#
# Conditional build:
#
%define		docver	4.0

Summary:	Virtual Network Computing
Summary(es.UTF-8):	Sistema de control remoto
Summary(pl.UTF-8):	Virtual Network Computing - zdalny desktop
Summary(pt_BR.UTF-8):	Sistema de controle remoto
Name:		vnc
Version:	4.1.2
%define		_ver	%(echo %{version} | tr . _)
Release:	0.2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://fresh.t-systems-sfr.com/linux/src/vnc-%{_ver}-unixsrc.tar.gz
#Source0:	http://www.realvnc.com/dist/%{name}-%{_ver}-unixsrc.tar.gz
# Source0-md5:	cf9a6fe8f592286b5e0fdde686504ffb
Source1:	http://www.realvnc.com/dist/%{name}-%{docver}-documentation.tar.gz
# Source1-md5:	eb3bf940b88cabb238580e2ba31b927b
# Source2:	svnc-0.1.tar.bz2
## Source2-md5:	af9a94e1d7795968ce7062fcbe31b84b
Source3:	vncviewer.desktop
Source4:	vnc.png
#Patch0:		%{name}-vncserver.patch
#Patch1:		%{name}-svncviewer.patch
#Patch2:		%{name}-imake.patch
#Patch3:		%{name}-svncviewer-pl_keys.patch
#Patch4:		%{name}-glibc_version.patch
#Patch5:		%{name}-malloc.patch
URL:		http://www.realvnc.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zlib-devel
Provides:	vnc-client
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

%description -l es.UTF-8
Sistema de control remoto.

%description -l pl.UTF-8
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu na dowolnej maszynie wyposażonej w odpowiedni
serwer. Dostępne są serwery dla Win32, Mac 8.x i X11, a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przeglądarce
działającej po HTTP).

Ten pakiet zawiera program wyświetlający ekran VNC (vncviewer).

%description -l pt_BR.UTF-8
VNC (Virtual Network Computing) ' um sistema de controle remoto que
permite visualizar um ambiente desktop nÇo somente da m quina onde o
VNC est  rodando, mas de qualquer lugar da Internet e de uma variedade
de arquiteturas. O VNC ' diferente de um servidor X em v rios
aspectos: nÇo salva nenhum estado no visualizador VNC, ' pequeno e
simples, ' de fato independente de plataforma, e um desktop pode ser
visto e usado por diversos visualizadores ao mesmo tempo.

%package server
Summary:	VNC X server
Summary(es.UTF-8):	Sistema de control remoto
Summary(pl.UTF-8):	X serwer VNC
Summary(pt_BR.UTF-8):	Sistema de controle remoto
Group:		X11/Applications/Networking
Requires:	XFree86-common
Requires:	XFree86-fonts-base
Requires:	XFree86-fonts
Requires:	%{name}-utils = %{version}-%{release}
Requires:	xinitrc-ng
Obsoletes:	tightvnc-server

%description server
VNC stands for Virtual Network Computing. It is, in essence, a remote
display system which allows you to view a computing 'desktop'
environment not only on the machine where it is running, but from
anywhere on the Internet and from a wide variety of machine
architectures.

This package contains VNC X server (Xvnc).

%description server -l es.UTF-8
Sistema de control remoto.

%description server -l pl.UTF-8
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu na dowolnej maszynie wyposażonej w odpowiedni
serwer. Dostępne są serwery dla Win32, Mac 8.x i X11, a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przeglądarce
działającej po HTTP).

Ten pakiet zawiera X serwer VNC (Xvnc).

%description server -l pt_BR.UTF-8
VNC (Virtual Network Computing) ' um sistema de controle remoto que
permite visualizar um ambiente desktop nÇo somente da m quina onde o
VNC est  rodando, mas de qualquer lugar da Internet e de uma variedade
de arquiteturas. O VNC ' diferente de um servidor X em v rios
aspectos: nÇo salva nenhum estado no visualizador VNC, ' pequeno e
simples, ' de fato independente de plataforma, e um desktop pode ser
visto e usado por diversos visualizadores ao mesmo tempo.

%package utils
Summary:	Additional utilities for VNC
Summary(pl.UTF-8):	Dodatkowe narzędzia do VNC
Group:		X11/Applications/Networking
Obsoletes:	tightvnc-utils

%description utils
This package contains additional VNC utilities: vncconnect and
vncpasswd. vncconnect tells Xvnc server to connect to a listening VNC
viewer. vncpasswd generates password file (both on server and
viewer side).

%description utils -l pl.UTF-8
Ten pakiet zawiera dodatkowe narzędzia VNC: vncconnect i vncpasswd.
vncconnect służy do połączenia serwera Xvnc z nasłuchującym
vncviewerem. vncpasswd służy to tworzenia pliku z hasłem (zarówno po
stronie serwera, jak i przeglądarki).

%package doc
Summary:	VNC documentation
Summary(pl.UTF-8):	Dokumentacja do VNC
Group:		Documentation

%description doc
This package contains documentation for VNC protocol, utilities etc.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację do VNC (protokołu, programów itp.).

%prep
%setup -q -n %{name}-4_1_2-unixsrc -a 1

%build
(cd unix;
%{__libtoolize};
%{__aclocal};
%{__autoconf};
%configure \
	--with-installed-zlib \
	--with-x 
)

(cd common;
%{__libtoolize};
%{__aclocal};
%{__autoconf};
%configure \
	--with-installed-zlib \
	--with-x 
)


%{__make} -C common
%{__make} -C unix

%install
rm -rf $RPM_BUILD_ROOT

cd unix

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

./vncinstall $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

#install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/vncviewer.desktop
%{_pixmapsdir}/vnc.png

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x0vncserver
%attr(755,root,root) %{_bindir}/vncserver
%{_datadir}/vnc
%{_mandir}/man1/x0vncserver.1*
%{_mandir}/man1/vncserver.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconfig
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconfig.1*
%{_mandir}/man1/vncpasswd.1*

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{docver}-documentation/* README
