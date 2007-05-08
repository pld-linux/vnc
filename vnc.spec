#
# Conditional build:
#
%define		docver		4.0
%define		java_vncver	4_1
%define         mesa_version    6.5.3
%define		xserver_ver	1.3.0.0

%define		xname		xorg-xserver-server

Summary:	Virtual Network Computing
Summary(es.UTF-8):	Sistema de control remoto
Summary(pl.UTF-8):	Virtual Network Computing - zdalny desktop
Summary(pt_BR.UTF-8):	Sistema de controle remoto
Name:		vnc
Version:	4.1.2
%define		_ver	%(echo %{version} | tr . _)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://fresh.t-systems-sfr.com/linux/src/vnc-%{_ver}-unixsrc.tar.gz
# Source0-md5:	cf9a6fe8f592286b5e0fdde686504ffb
Source1:	http://www.realvnc.com/dist/%{name}-%{docver}-documentation.tar.gz
# Source1-md5:	eb3bf940b88cabb238580e2ba31b927b
Source2:	http://fresh.t-systems-sfr.com/unix/src/misc/vnc-%{java_vncver}-javasrc.tar.gz
# Source2-md5:	9407ce1f215aefca77bef12670745280
Source3:	vncviewer.desktop
Source4:	vnc-16x16.png
Source5:	vnc-24x24.png
Source6:	vnc-48x48.png
Source7:	vncserver.init
Source8:	vncserver.sysconfig
#Sources and patches above 100 belong to xserver
Source100:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{xserver_ver}.tar.bz2
# Source100-md5:	a51a7d482e3c689394755bb17bda8526
Source101:	http://dl.sourceforge.net/mesa3d/MesaLib-%{mesa_version}.tar.bz2
# Source101-md5:	46359457147c469745f24b5074a186f0
Source102:	xserver.pamd
Patch0:		%{name}-cookie.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-use-fb.patch
Patch3:		%{name}-xclients.patch
Patch4:		%{name}-idle.patch
Patch5:		%{name}-via.patch
Patch6:		%{name}-build.patch
Patch7:		%{name}-fPIC.patch
Patch8:		%{name}-restart.patch
Patch9:		%{name}-vncpasswd.patch
Patch10:	%{name}-def.patch
Patch11:	%{name}-modular-xorg.patch
Patch12:	%{name}-nohttpd.patch
Patch13:	%{name}-fontpath.patch
Patch14:	%{name}-s390.patch
Patch15:	%{name}-viewer-reparent.patch
Patch16:	%{name}-64bit.patch
Patch17:	%{name}-select.patch
Patch18:	%{name}-null-interface.patch
Patch19:	%{name}-ppc64.patch
Patch20:	%{name}-opengl.patch
Patch21:	%{name}-newfbsize.patch
Patch22:	%{name}-188169.patch
Patch23:	%{name}-210617.patch
Patch24:	%{name}-102434.patch
Patch25:	%{name}-config.patch
Patch26:	%{name}-render.patch
#Sources and patches above 100 belong to xserver
Patch100:	%{xname}-ncurses.patch
Patch101:	%{xname}-xwrapper.patch
# nasty hack for http://gcc.gnu.org/bugzilla/show_bug.cgi?id=30052
Patch102:	%{xname}-gcc-x86_64-workaround.patch
Patch103:	%{xname}-drop-GLinterface.patch
Patch104:	%{xname}-mesa.patch
URL:		http://www.realvnc.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	gcc-java
BuildRequires:	fastjar
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.3
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
BuildRequires:	xorg-proto-fixesproto-devel >= 4.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.8
BuildRequires:	xorg-proto-inputproto-devel >= 1.4
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-randrproto-devel >= 1.2
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1.0
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
Requires:	%{name}-utils = %{version}-%{release}
Requires:	policycoreutils
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

%package xorg-ext
Summary:	VNC extension for XServer
Summary(pl.UTF-8):	Rozszerzenie VNC dla servera Xów
Group:		X11/Applications/Networking
Requires:	%{name}-utils = %{version}-%{release}
Requires:	xorg-xserver-server = %{xserver_ver}

%description xorg-ext
VNC extension for XServer.

%description xorg-ext -l pl.UTF-8
Rozszerzenie VNC dla servera Xów.

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
%setup -q -n %{name}-4_1_2-unixsrc -a1 -a2 -a101
cd unix
tar -xkjf %{SOURCE100}
ln -sf xorg-server-* xorg-server
cd xorg-server
%patch100 -p1
%patch101 -p0
%ifarch %{x8664} i486
%patch102 -p1
%endif
%patch103 -p2
%patch104 -p2
cd ../..

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
#%patch13 -p3 -b .fontpath
#%patch14 -p3 -b .s390
%patch15 -p1
%patch16 -p1
%patch17 -p1
#patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

cp -a \
	unix/xc/programs/Xserver/vnc/Xvnc/xvnc.cc \
	unix/xc/programs/Xserver/Xvnc.man \
	unix/xc/programs/Xserver/vnc/*.{h,cc} \
	unix/xorg-server-*/{cfb/cfb.h,fb/fb.h,fb/fbrop.h} \
	unix/xorg-server-*/hw/vnc/

sed -i -e 's,xor,c_xor,' -e 's,and,c_and,' \
	unix/xorg-server-*/hw/vnc/{cfb,fb,fbrop}.h

%build
cd unix
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-installed-zlib \
	--with-x 
cd ..

cd common
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-installed-zlib \
	--with-x
cd ..

cd vnc-%{java_vncver}-javasrc/java
make JAVAC="gcj -C" JAR=fastjar
cd ../..

%{__make} -C unix
%{__make} -C common

cd unix/xorg-server
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--enable-dga \
	--disable-builddocs \
	--disable-lbx \
	--disable-xevie \
	--disable-dmx \
	--disable-dri \
	--disable-xprint \
	--disable-static \
	--disable-xorgcfg \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-mesa-source="`pwd`/../../Mesa-%{mesa_version}" \
	--with-xkb-output=/var/lib/xkb

cp -f %{_bindir}/libtool .
%{__make}
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

cd unix

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_libdir}/xorg/modules/extensions}
./vncinstall $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_libdir}/xorg/modules/extensions}

install -d $RPM_BUILD_ROOT%{_datadir}/vnc/classes
cp -a ../vnc-%{java_vncver}-javasrc/java/{index.vnc,logo150x150.gif,vncviewer.jar} \
	$RPM_BUILD_ROOT%{_datadir}/vnc/classes

install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,24x24,48x48}/apps
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/vnc.png
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/vnc.png
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/vnc.png

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/vncserver
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/vncserver

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add vncserver
%service vncserver restart "Xvnc daemon"

%preun server
if [ "$1" = "0" ]; then
	%service vncserver stop
	/sbin/chkconfig --del vncserver
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/vncviewer.desktop
%{_datadir}/icons/hicolor/*/apps/vnc.png

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvnc
%attr(755,root,root) %{_bindir}/x0vncserver
%attr(755,root,root) %{_bindir}/vncserver
%attr(754,root,root) /etc/rc.d/init.d/vncserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vncserver
%{_datadir}/vnc
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/x0vncserver.1*
%{_mandir}/man1/vncserver.1*
%{_mandir}/man1/x0vncserver.1*

%files xorg-ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libvnc.so

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconfig
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconfig.1*
%{_mandir}/man1/vncpasswd.1*

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{docver}-documentation/* README
