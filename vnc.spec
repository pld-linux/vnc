Summary:	Virtual Network Computing
Summary(pl):	Virtual Network Computing -- zdalny desktop
Name:		vnc
Version:	3.3.3r2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.uk.research.att.com/vnc/dist/%{name}-%{version}_unixsrc.tgz
Source1:	http://www.uk.research.att.com/vnc/dist/%{name}-latest_doc.tgz
Patch0:		http://www.ce.cctpu.edu.ru/vnc/preview/%{name}-%{version}-unix-tight-1.1p4.patch.gz
Patch1:		%{name}-vncserver.patch
Patch2:		%{name}-ppc.patch
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
obrazu zdalnego desktopu z dowolnej maszynie wyposa�nej w odpowiedni
serwer. Dost�pne s� serwery dla Win32, Mac 8.x i X11 a klienty dla
Win32, Mac 8.x, X11, Windows CE, BeOS i Java (np. w przegl�darce
dzia�aj�cej po HTTP).

%prep
%setup -q -c -a 1

cd %{name}_unixsrc
%patch0 -p1

%patch1 -p1
%ifarch ppc
%patch2 -p1
%endif
rm -rf vnc_docs/*~ vnc_docs/*,v

%build
cd %{name}_unixsrc

xmkmf
%{__make} CDEBUGFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" World
cd Xvnc
%{__make} CDEBUGFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" World

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/vnc/classes}

cd %{name}_unixsrc

./vncinstall $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

gzip -9nf $RPM_BUILD_DIR/%{name}-%{version}/vnc_unixsrc/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc vnc_docs/* vnc_unixsrc/README.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/vnc
