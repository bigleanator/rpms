Name:           slade
Version:        3.2.6
Release:        %autorelease
Summary:        It's a Doom editor

License:        GPLv2

URL:            https://slade.mancubus.net
Source0:        https://github.com/sirjuddington/SLADE/archive/refs/tags/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/bigleanator/rpms/main/slade/wayland-.desktop-compat.patch

Patch0:         wayland-.desktop-compat.patch

#BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake
BuildRequires:  mold
BuildRequires:  python3-ninja
BuildRequires:  freeglut-devel
BuildRequires:  bzip2-devel
BuildRequires:  libcurl-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  freeimage-devel
BuildRequires:  ftgl-devel
BuildRequires:  glew-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  SFML-devel
BuildRequires:  lua-devel
BuildRequires:  fmt-devel
BuildRequires:  gtk3-devel
BuildRequires:  wxGTK-devel

# sudo dnf install gcc-c++ cmake freeglut-devel git bzip2-devel libcurl-devel fluidsynth-devel freeimage-devel
# ftgl-devel glew-devel gstreamer1-devel gstreamer1-plugins-base-devel libmodplug SFML-devel lua-devel fmt-devel
#gtk3-devel wxGTK3-devel wxGTK3-gl wxGTK3-media wxGTK3-webview

Requires:       fluidsynth
Requires:       fluidsynth-libs
Requires:       libmodplug
Requires:       freeglut
Requires:       libcurl
Requires:       bzip2
Requires:       freeimage
Requires:       ftgl
Requires:       glew
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       SFML
Requires:       lua
Requires:       fmt
Requires:       wxGTK-gl
Requires:       wxGTK-media
Requires:       wxGTK-webview


%description
SLADE3 is a modern editor for Doom-engine based games and source ports.
It has the ability to view, modify, and write many different game-specific formats,
and even convert between some of them, or from/to other generic formats such as PNG.

%prep
%autosetup -n SLADE-%{version}


%build
#mkdir dist
#%cmake -DNO_WEBVIEW=ON
#cd dist
#cmake .. -DNO_WEBVIEW=ON
%cmake -DCMAKE_EXE_LINKER_FLAGS="-fuse-ld=mold" -DCMAKE_SHARED_LINKER_FLAGS="-fuse-ld=mold" -DNO_WEBVIEW=ON
%cmake_build


%install
#cd %{_builddir}/dist
#%make_install
%cmake_install


%files
%license
%{_bindir}/slade
# slade-3.2.6.fc40.x86_64.debug
# slade-3.2.6-1.fc40.x86_64.debug
%{_prefix}/lib/debug/usr/bin/slade-%{version}-%{release}.%{_arch}.debug
%{_datadir}/applications/net.mancubus.SLADE.desktop
%{_datadir}/icons/hicolor/scalable/apps/net.mancubus.SLADE.svg 
%{_datadir}/metainfo/net.mancubus.SLADE.metainfo.xml
%{_datadir}/slade3/slade.pk3
#/usr/bin/slade
#/usr/lib/debug/usr/bin/slade-3.2.6-1.fc40.x86_64.debug
#/usr/share/applications/net.mancubus.SLADE.desktop
#/usr/share/icons/hicolor/scalable/apps/net.mancubus.SLADE.svg
#/usr/share/metainfo/net.mancubus.SLADE.metainfo.xml
#/usr/share/slade3/slade.pk3

%changelog
* Mon Jul 01 2024 bigleanator <98368716+bigleanator@users.noreply.github.com>
- Initial version
