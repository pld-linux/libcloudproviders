#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Cloud providers DBus API library
Summary(pl.UTF-8):	Biblioteka API DBus usług dostawców chmurowych
Name:		libcloudproviders
Version:	0.2.5
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://gitlab.gnome.org/World/libcloudproviders/tags
Source0:	https://gitlab.gnome.org/World/libcloudproviders/uploads/32bb0a808c397d55b6d72c61540c0171/%{name}-%{version}.tar.xz
# Source0-md5:	5c6f15fca82c9deb27a16ea956afdc15
URL:		https://gitlab.gnome.org/World/libcloudproviders
BuildRequires:	gcc >= 5:3.2
BuildRequires:	glib2-devel >= 1:2.51.2
BuildRequires:	gtk-doc
BuildRequires:	meson >= 0.40.0
BuildRequires:	ninja
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcloudproviders is a DBus API that allows cloud storage sync clients
to expose their services. Clients such as file managers and desktop
environments can then provide integrated access to the cloud providers
services.

%description -l pl.UTF-8
libcloudproviders to API DBus pozwalające klientom synchronizacji z
przestrzenią dyskową w chmurze eksponować swoje usługi. Klienci tacy
jak zarządcy plików czy środowiska graficzne mogą zapewniać
zintegrowany dostęp do usług dostawców chmurowych.

%package devel
Summary:	Header files for cloudproviders library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cloudproviders
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.51.2

%description devel
Header files for cloudproviders library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cloudproviders.

%package apidocs
Summary:	API documentation for cloudproviders library
Summary(pl.UTF-8):	Dokumentacja API biblioteki cloudproviders
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for cloudproviders library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki cloudproviders.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Denable-gtk-doc=true}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%attr(755,root,root) %{_libdir}/libcloudproviders.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcloudproviders.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcloudproviders.so
%{_includedir}/cloudproviders
%{_pkgconfigdir}/cloudproviders.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libcloudproviders
%endif
