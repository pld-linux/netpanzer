#
# TODO: everything :>
#	OK, now serious
#	-jam instakk
#	-install the data
#
Summary:	Online multiplayer tactical warfare
Name:		netpanzer
Version:	0.1.3
Release:	0.0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	bd593ff24f2228c574f89a61e9921b83
Source1:	http://download.berlios.de/%{name}/%{name}data-%{version}.tar.bz2
# Source1-md5:	3080e48be7cb28bdb8f8b26dd84b3755
URL:		http://netpanzer.berlios.de/
BuildRequires:	jam
BuildRequires:	physfs >= 1.9
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netPanzer is an online multiplayer tactical warfare game designed for play                                     
across the Internet and over LAN systems. netPanzer is designed for FAST ACTION                                
combat -- it is not another resource management clone. In fact, there aren't                                   
any resources at all.


%prep
%setup -q -a1

%build
%configure \
	--prefix=%{_prefix}
jam

%install
rm -rf $RPM_BUILD_ROOT

jam install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
