Name:           alsa-oss
Version:        1.1.8
Release:        %autorelease
Summary:        OSS compatibility library

License:        GPLv2

URL:            https://www.alsa-project.org
Source0:        https://www.alsa-project.org/files/pub/oss-lib/%{name}-%{version}.tar.bz2



BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  alsa-lib-devel
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  glibc
BuildRequires:  make

Requires:       alsa-lib

%description
Makes OSS apps speak ALSA

%prep
%autosetup


%build
autoreconf -fiv
%configure --prefix=/usr
%make_build

%install
%make_install

%files
%{_bindir}/aoss
%{_includedir}/oss-redir.h
%{_libdir}/libalsatoss.a
%{_libdir}/libalsatoss.so
%{_libdir}/libalsatoss.so.0
%{_libdir}/libalsatoss.so.0.0.0
%{_libdir}/libaoss.a
%{_libdir}/libaoss.so
%{_libdir}/libaoss.so.0
%{_libdir}/libaoss.so.0.0.0
%{_libdir}/libossredir.a
%{_mandir}/man1/aoss.1.gz

%changelog
* Thu Jul 11 2024 bigleanator <98368716+bigleanator@users.noreply.github.com>
- Initial version
