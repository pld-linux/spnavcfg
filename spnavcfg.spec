# TODO: privileges (needs to modify /etc/spnavrc and send signals to spacenavd)
#       (original solution is suid root, maybe spacenavd could run as other user?)
Summary:	Spacenav daemon interactive configuration program
Summary(pl.UTF-8):	Program do interaktywnej konfiguracji demon Spacenav
Name:		spnavcfg
Version:	0.3
Release:	0.1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz
# Source0-md5:	ac4ac49b07c4a4dbfa6ba1cd0d357273
Patch0:		%{name}-make.patch
URL:		http://spacenav.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spacenav daemon interactive configuration program.

%description -l pl.UTF-8
Program do interaktywnej konfiguracji demon Spacenav.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CC="%{__cc}" \
	opt="%{rpmcflags}" \
	ldopt="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/spnavcfg
%{_iconsdir}/hicolor/*x*/apps/spnavcfg.png
