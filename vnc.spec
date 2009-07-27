
%define		docver		4.0
%define		java_vncver	4_1
%define		mesa_version    7.2
%define		xserver_ver	1.5.3
%define		xname		xorg-xserver-server
%define		_ver		%(echo %{version} | tr . _)

Summary:	Virtual Network Computing
Summary(es.UTF-8):	Sistema de control remoto
Summary(pl.UTF-8):	Virtual Network Computing - zdalny desktop
Summary(pt_BR.UTF-8):	Sistema de controle remoto
Name:		vnc
Version:	4.1.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://be.lunar-linux.org/lunar/mirrors/%{name}-%{_ver}-unixsrc.tar.gz
# Source0-md5:	a119f3c75ad2767c0588260e2abe39be
Source1:	http://www.realvnc.com/dist/%{name}-%{docver}-documentation.tar.gz
# Source1-md5:	eb3bf940b88cabb238580e2ba31b927b
Source2:	http://fresh.t-systems-sfr.com/unix/src/misc/%{name}-%{java_vncver}-javasrc.tar.gz
# Source2-md5:	9407ce1f215aefca77bef12670745280
Source3:	%{name}viewer.desktop
Source4:	%{name}-16x16.png
Source5:	%{name}-24x24.png
Source6:	%{name}-48x48.png
Source7:	%{name}server.init
Source8:	%{name}server.sysconfig
Source9:	%{name}-Makefile.am
#Sources and patches above 100 belong to xserver
Source100:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{xserver_ver}.tar.bz2
# Source100-md5:	308971036e25250e7fe3cccfd5a120f8
Source101:	http://dl.sourceforge.net/mesa3d/MesaLib-%{mesa_version}.tar.bz2
# Source101-md5:	04d379292e023df0b0266825cb0dbde5
Source102:	xserver.pamd
Patch0:		%{name}-cookie.patch
Patch1:		%{name}-gcc4.patch
Patch2:		%{name}-use-fb.patch
Patch3:		%{name}-xclients.patch
Patch4:		%{name}-idle.patch
Patch5:		%{name}-via.patch
Patch6:		%{name}-restart.patch
Patch7:		%{name}-vncpasswd.patch
Patch8:		%{name}-modular-xorg.patch
Patch9:		%{name}-nohttpd.patch
Patch10:	%{name}-viewer-reparent.patch
Patch11:	%{name}-64bit.patch
Patch12:	%{name}-select.patch
Patch13:	%{name}-newfbsize.patch
Patch14:	%{name}-102434.patch
Patch15:	%{name}-config.patch
Patch16:	%{name}-render.patch
Patch17:	%{name}-autotools.patch
Patch18:	%{name}-autotools-compile.patch
Patch19:	%{name}-always_use_fb.patch
Patch20:	%{name}-vsnprintf.patch
Patch21:	%{name}-24bit.patch
Patch22:	%{name}-gcc43.patch
Patch23:	%{name}-xorg.patch
Patch24:	%{name}-xinerama.patch
Patch25:	%{name}-privates.patch
Patch26:	%{name}-mieq.patch
Patch27:	%{name}-allocate.patch
Patch28:	%{name}-paint.patch
Patch29:	%{name}-selections.patch
Patch30:	%{name}-manminor.patch
Patch31:	%{name}-clipboard.patch
Patch32:	%{name}-scrollbars.patch
Patch33:	%{name}-bounds.patch
Patch34:	%{name}-includes.patch
Patch35:	%{name}-viewerIPv6.patch
Patch36:	%{name}-rh212985.patch
Patch37:	%{name}-build.patch
#Sources and patches above 100 belong to xserver
Patch100:	%{xname}-ncurses.patch
Patch101:	%{xname}-xwrapper.patch
URL:		http://www.realvnc.com/
#  https://rhn.redhat.com/errata/RHSA-2009-0261.html
# Patch in Fedora repo:
BuildRequires:	security(CVE-2008-4770)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java
BuildRequires:	jar
BuildRequires:	libdrm-devel >= 2.4.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	Mesa-libGL-devel >= 7.2
BuildRequires:	pixman-devel >= 0.9.5
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-bigreqsproto-devel
BuildRequires:	xorg-proto-compositeproto-devel >= 0.3
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
BuildRequires:	xorg-proto-fixesproto-devel >= 4.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.9
BuildRequires:	xorg-proto-inputproto-devel >= 1.4
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-randrproto-devel >= 1.2
BuildRequires:	xorg-proto-recordproto-devel
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1.0
BuildRequires:	xorg-proto-trapproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86bigfontproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	zlib-devel
Provides:	vnc-client
Conflicts:	tightvnc
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
Conflicts:	tightvnc-server

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
Conflicts:	tightvnc-utils

%description utils
This package contains additional VNC utilities: vncconnect and
vncpasswd. vncconnect tells Xvnc server to connect to a listening VNC
viewer. vncpasswd generates password file (both on server and viewer
side).

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
%setup -q -n %{name}-%{_ver}-unixsrc -a1 -a2 -a101
cd unix
tar -xkjf %{SOURCE100}
ln -sf xorg-server-* xorg-server
cd xorg-server
%patch100 -p1
%patch101 -p0

# xserver uses pixman-1 API/ABI so put that explictly here
# update: we use local pixman.h copy too, see below
sed -i -e 's#<pixman\.h>#"pixman.h"#g' fb/fb.h include/miscstruct.h render/picture.h

rm hw/xprint/{miinitext-wrapper,dpmsstubs-wrapper}.c
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
%patch13 -p1 
%patch14 -p1 
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

mkdir -p unix/xorg-server/hw/vnc
cp %{SOURCE9} unix/xorg-server/hw/vnc/Makefile.am
cp -a \
	unix/xc/programs/Xserver/vnc/Xvnc/xvnc.cc \
	unix/xc/programs/Xserver/Xvnc.man \
	unix/xc/programs/Xserver/vnc/*.{h,cc} \
	unix/xorg-server/{cfb/cfb.h,fb/fb.h,fb/fbrop.h} \
	unix/xorg-server/hw/vnc/
cp /usr/include/pixman-1/pixman.h \
	unix/xorg-server/include

# symbol clash with vnc code
sed -i -e 's,xor,c_xor,' -e 's,and,c_and,' \
	unix/xorg-server/{hw/vnc/{cfb,fb,fbrop}.h,include/pixman.h}

cd unix/xorg-server/hw/vnc
%patch25 -p1
cd -
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1

%build
cd common
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
cd ..

cd unix
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
cd ..

cd vnc-%{java_vncver}-javasrc/java
%{__make} JAVAC="gcj -C" JAR=jar
cd ../..

cd unix/xorg-server
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	\
	--enable-glx \
	--enable-install-libxf86config \
	--enable-xcsecurity \
	\
	--disable-composite \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-dri2 \
	--disable-dmx \
	--disable-kdrive \
	--disable-static \
	--disable-xephyr \
	--disable-xevie \
	--disable-xnest \
	--disable-xorg \
	--disable-xorgcfg \
	--disable-xprint \
	--disable-xtrap \
	--disable-xvfb \
	--disable-xwin \
	\
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-dri-driver-path=%{_libdir}/dri \
	--with-fontdir=%{_datadir}/X11/fonts \
	--with-mesa-source="`pwd`/../../Mesa-%{mesa_version}" \
	--with-pic \
	--with-rgb-path=%{_datadir}/X11/rgb \
	--with-xkb-output=%{_localstatedir}/lib/xkb

cp -f %{_bindir}/libtool .
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/drm"
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

cd common
make install DESTDIR=$RPM_BUILD_ROOT

cd ../unix

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
for f in xorg-server/hw/vnc/Xvnc vncviewer/vncviewer vncpasswd/vncpasswd \
	vncconfig/vncconfig vncserver x0vncserver/x0vncserver
do
	cp -pf $f.man $RPM_BUILD_ROOT%{_mandir}/man1/`basename $f.1`
done
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cp vncserver $RPM_BUILD_ROOT/usr/bin

cd xorg-server/hw/vnc
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ../../../

install -d $RPM_BUILD_ROOT%{_datadir}/vnc/classes
cp -a ../vnc-%{java_vncver}-javasrc/java/{index.vnc,logo150x150.gif,vncviewer.jar} \
	$RPM_BUILD_ROOT%{_datadir}/vnc/classes

install -d $RPM_BUILD_ROOT{%{_datadir}/icons/hicolor/{16x16,24x24,48x48}/apps,%{_desktopdir}}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/vncviewer.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/vnc.png
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/vnc.png
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/vnc.png

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/vncserver
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/vncserver

# remove unwanted files
rm -f $RPM_BUILD_ROOT%{_libdir}/librfb.*a
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libvnc.*a

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
%{_iconsdir}/hicolor/*/apps/vnc.png

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
%{_libdir}/librfb.*
%{_mandir}/man1/vncconfig.1*
%{_mandir}/man1/vncpasswd.1*

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{docver}-documentation/* README
