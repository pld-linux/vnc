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
BuildRoot: /tmp/%{name}-%{version}-root
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
install -d $RPM_BUILD_ROOT/usr/share/vnc/classes
./vncinstall $RPM_BUILD_ROOT/usr/X11R6/bin
install -m644 classes/* $RPM_BUILD_ROOT/usr/share/vnc/classes
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
/usr/share/vnc/classes/
%doc doc/
%doc README

%changelog
* Thu Feb  4 1999 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
 [3.3.2r3-1d]
- added documentation 
- build angainst glibc 2.1 
- added mode detail %attr in %files section 
- Polish language spec translation

* Sat Nov 7 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
  [3.3.2r2-1a]
- Add patch for compiling against LinuxPPC.

* Sat Jul 25 1998 Arne Coucheron <arneco@online.no>
  [3.3.2r2-1]

* Mon Jul 06 1998 Arne Coucheron <arneco@online.no>
  [3.3.2-3]
- it would have been nice if people updating the package would follow
  common sense and do it so using existing ones, and also update their
  changes in the changelog, but I guess some find this rule hard to follow
- binaries moved back to /usr/X11R6/bin

* Tue May 26 1998 Arne Coucheron <arneco@online.no>
  [3.3.2-1]
- moved java classes to /usr/share/vnc/classes
- moved binaries to /usr/bin
- using predefined %%{name} and %%{version}
- using %defattr in filelist, this means that rpm 2.5 is required to build

* Tue Mar 17 1998 Arne Coucheron <arneco@online.no>
  [3.3.1-4]
- added a new font patch, hopefully this works better (Thanks to Gábor J.Tóth)

* Sun Mar 01 1998 Arne Coucheron <arneco@online.no>
  [3.3.1-3]
- using buildroot and %attr macros
- added patch to make it build against glibc
- added patch to make it find the fonts on RH5
