# TODO:
# - check why directories in data package are (example):
# %{_datadir}/%{name}/units/pics/pak/pics/pak/WolfTSSD.pak not
# %{_datadir}/%{name}/units/pics/pak/WolfTSSD.pak
# This is the reason that game doesen't run proprty

Summary:	Online multiplayer tactical warfare
Summary(de):	Online multiplayer Echtzeitstrategiespiel
Summary(pl):	Sieciowa gra strategiczna czasu rzeczywistego
Name:		netpanzer
Version:	0.8
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	c08c1b703eac533407db02510deca68e
Source1:	http://download.berlios.de/%{name}/%{name}-data-%{version}.tar.bz2
# Source1-md5:	d2dbd5a6c38a181fa3b6aa9a68c81d2f
Source2:	%{name}-install.jam
Source3:	%{name}.desktop
Source4:	%{name}.png
URL:		http://netpanzer.berlios.de/
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	boost-jam
BuildRequires:	libstdc++-devel >= 5:3.2.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	physfs-devel >= 0.1.9
# only for ac/am; --with-wx-config must be passed to really use wx*
BuildRequires:	wxWindows-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netPanzer is an online multiplayer tactical warfare game designed for
play across the Internet and over LAN systems. netPanzer is designed
for FAST ACTION combat - it is not another resource management clone.
In fact, there aren't any resources at all.

%description -l de
netPanzer ist ein online multiplay Echtzeitstrategiespiel designt f�r
schnelle aktionlastige K�mpfe. Das Spielprinzip konzentriert sich auf
das wesentliche - kein Resourcenmanagemenet wird ben�tigt, stattdessen 
kommt es auf schnelle taktische Bewegungen und Einheiten-Management in
Echtzeit an. Die K�mpfe sind schnell und dauern lange an, weil zerst�rte 
Spieler mit einer Reihe neuer Einheiten neustarten. Spieler k�nnen einem
Spiel jederzeit beitreten oder es verlassen.

%description -l pl
netPanzer jest sieciow� gr� strategiczn� czasu rzeczywistego
zaprojektowany na szybk� rozgrywk�. Nie znajdziesz tutaj zarz�dzania
zasobami, jedynie szybkie bitwy i d�ug� wojn�, gdy� zniszczeni gracze
pojawiaj� si� zn�w w grze z kilkoma nowymi jednostkami. Gracze mog� w
dowolnym momencie do��czy� do rozgrywki lub j� opu�ci�.

%package data
Summary:	Data files for netPanzer
Summary(de):	Daten f�r netPanzer
Summary(pl):	Pliki z danymi dla netPanzera
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data
Graphic and sound files required by netPanzer.

%description data -l de
Grafik- und Sounddateien f�r netPanzer.

%description data -l pl
Pliki graficzne i d�wi�kowe dla netPanzera.

%prep
%setup -q -a1

%build
rm -rf $RPM_BUILD_ROOT
rm -f %{name}data-%{_dataver}/mk/jam/install.jam

install %{SOURCE2} %{name}-data-%{version}/mk/jam/install.jam

cp -f /usr/share/automake/config.* mk/autoconf
%{__aclocal} -I mk/autoconf
%{__autoconf}
%configure
jam

cd %{name}-data-%{version}

cp -f /usr/share/automake/config.* mk/autoconf
%{__aclocal} -I mk/autoconf
%{__autoconf}
%configure
jam

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_datadir}/netpanzer}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

export DESTDIR=$RPM_BUILD_ROOT
jam install
cd %{name}-data-%{version}
jam install

for i in {cache,maps,pics,powerups,sound,units,wads};
do
  mv $RPM_BUILD_ROOT%{_datadir}/$i $RPM_BUILD_ROOT%{_datadir}/netpanzer/
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/netpanzer*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}
