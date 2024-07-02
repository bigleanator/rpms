Name:           zdbsp
Version:        1.19
Release:        %autorelease
Summary:        ZDBSP is ZDoom's internal node builder.

License:        GPLv2

URL:            https://github.com/rheit/zdbsp
Source0:        https://github.com/rheit/zdbsp/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/bigleanator/rpms/raw/main/zdbsp/installable.patch

Patch0:         installable.patch


#BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  cmake-rpm-macros
BuildRequires:  cmake


# sudo dnf install gcc-c++ cmake freeglut-devel git bzip2-devel libcurl-devel fluidsynth-devel freeimage-devel
# ftgl-devel glew-devel gstreamer1-devel gstreamer1-plugins-base-devel libmodplug SFML-devel lua-devel fmt-devel
#gtk3-devel wxGTK3-devel wxGTK3-gl wxGTK3-media wxGTK3-webview




%description
ZDBSP is ZDoom's internal node builder.

%prep
%autosetup


%build
#cmake .. -DNO_WEBVIEW=ON
%cmake
%cmake_build


%install
%cmake_install

%files
%{_bindir}/zdbsp

%changelog
* Tue Jul 02 2024 bigleanator <98368716+bigleanator@users.noreply.github.com>
- Initial version
