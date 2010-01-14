Summary:	Amap - a next-generation scanning tool
Summary(pl.UTF-8):	Amap - skaner "następnej generacji"
Name:		amap
Version:	5.2
Release:	3
License:	GPL v2 with exceptions (see LICENCE.AMAP)
Group:		Networking
Source0:	http://freeworld.thc.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e3b1f5ebd24aac03aacb38ec183eb426
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-path.patch
Patch2:		%{name}-ldflags.patch
Patch3:		%{name}-new-homepage.patch
Patch4:		%{name}-system-pcre.patch
URL:		http://www.thc.org/thc-amap/
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	sed >= 4.0
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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{__sed} -i 's@LIBDIRS=.*@LIBDIRS="%{_libdir} %{_libdir}/openssl"@' configure

%build
./configure \
	--prefix=%{_prefix}

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO LICENCE.AMAP
%attr(755,root,root) %{_bindir}/amap
%attr(755,root,root) %{_bindir}/amap6
%attr(755,root,root) %{_bindir}/amapcrap
%{_mandir}/man1/amap.1*
%{_datadir}/%{name}
