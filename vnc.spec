Summary:	Virtual Network Computing
Summary(pl):	Virtual Network Computing -- zdalny desktop
Summary(pt_BR):	Sistema de controle remoto.
Summary(es):	Sistema de control remoto.
Name:		vnc
Version:	3.3.3r2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_unixsrc.tgz
Source1:	http://www.uk.research.att.com/vnc/dist/%{name}-latest_doc.tgz
Patch0:		http://www.ce.cctpu.edu.ru/vnc/preview/%{name}-%{version}-unix-tight-1.1p4.patch.gz
Patch1:		%{name}-vncserver.patch
Patch2:		%{name}-ppc.patch
Patch3:		%{name}-ComplexProgramTargetNoMan.patch
URL:		http://www.uk.research.att.com/vnc/
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
VNC stands for Virtual Network Computing. It is, in essence, a remote
display system which allows you to view a computing 'desktop'
environment not only on the machine where it is running, but from
anywhere on the Internet and from a wide variety of machine
architectures.

%description -l pl
VNC oznacza Virtual Network Computing. Pakiet ten pozwala na uzyskanie
obrazu zdalnego desktopu na dowolnej maszynie wyposaønej w odpowiedni
serwer. DostÍpne s± serwery dla Win32, Mac 8.x i X11, a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl±darce
dzia≥aj±cej po HTTP).

%description -l pt_BR
VNC (Virtual Network Computing) ' um sistema de controle remoto que
permite visualizar um ambiente desktop n«o somente da m†quina onde o
VNC est† rodando, mas de qualquer lugar da Internet e de uma variedade
de arquiteturas. O VNC ' diferente de um servidor X em v†rios
aspectos: n«o salva nenhum estado no visualizador VNC, ' pequeno e
simples, ' de fato independente de plataforma, e um desktop pode ser
visto e usado por diversos visualizadores ao mesmo tempo.

%description -l es
Sistema de control remoto.

%prep
%setup -q -c -a 1

cd %{name}_unixsrc
%patch0 -p1
%patch1 -p1
%ifarch ppc
%patch2 -p1
%endif
%patch3 -p1


%build
cd %{name}_unixsrc

xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}" World
cd Xvnc
%{__make} CDEBUGFLAGS="%{rpmcflags}" World

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes}

cd %{name}_unixsrc

./vncinstall $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

gzip -9nf $RPM_BUILD_ROOT%{name}-%{version}/vnc_unixsrc/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc vnc_docs/*.{html,jpg,html,htm,dtd,pdf,css,GIF} vnc_unixsrc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/vnc
