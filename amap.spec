Summary:	Amap is a next-generation scanning tool
Summary(pl):	Amap jest skanerem "nastêpnej generacji"
Name:		amap
Version:	4.7
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://thc.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	c2ce244321b0b7b5eb28fdc785452b9a
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-path.patch
URL:		http://www.thc.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amap is a next-generation scanning tool, which identifies applications
and services even if they are not listening on the default port by
creating a bogus-communication and analyzing the responses.

%description -l pl
Amap jest skanerem "nastêpnej generacji", który identyfikuje aplikacje
i serwisy nawet gdy nie nasluchuj± na domy¶lnych portach poprzez
tworzenie pseudo komunikacji i analizie odpowiedzi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure
%{__make} strip

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/amap.1.gz
%{_datadir}/%{name}
