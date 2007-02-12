Summary:	Amap - a next-generation scanning tool
Summary(pl.UTF-8):   Amap - skaner "następnej generacji"
Name:		amap
Version:	5.2
Release:	1
License:	GPL
Group:		Networking
Source0:	http://thc.segfault.net/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e3b1f5ebd24aac03aacb38ec183eb426
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-path.patch
URL:		http://thc.segfault.net/thc-amap/
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amap is a next-generation scanning tool, which identifies applications
and services even if they are not listening on the default port by
creating a bogus-communication and analyzing the responses.

%description -l pl.UTF-8
Amap jest skanerem "następnej generacji", który identyfikuje aplikacje
i usługi nawet gdy nie nasłuchują na domyślnych portach poprzez
tworzenie pseudo komunikacji i analizie odpowiedzi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix}
%{__make} strip

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DATADIR=%{_datadir}/%{name} \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/amap.1*
%{_datadir}/%{name}
