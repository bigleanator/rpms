Name:           crispy-doom
Version:        6.0
Release:        %autorelease
Summary:        A limit removing fork of chocolate doom 

License:        GPLv2
URL:            https://github.com/fabiangreffrath/crispy-doom
Source0:        https://github.com/fabiangreffrath/crispy-doom/archive/refs/tags/crispy-doom-6.0.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  zlib-ng-devel
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fluidsynth-devel

#checking for zlib... no
#checking for samplerate >= 0.1.8... no
#checking for libpng >= 1.2.50... no
#checking for fluidsynth >= 2.2.0... no

Requires:       SDL2_mixer
Requires:       SDL2_net
Requires:       zlib-ng
Requires:       libpng
Requires:       libsamplerate
Requires:       fluidsynth
Requires:       fluidsynth-libs


%description
Crispy Doom is a friendly fork of Chocolate Doom that provides a higher display resolution,
removes the static limits of the Doom engine and offers further optional visual, tactical
and physical enhancements while remaining entirely config file, savegame, netplay
and demo compatible with the original.

%prep
%autosetup -n crispy-doom-crispy-doom-%{version}


%build
autoreconf -fiv
%configure
%make_build


%install
%make_install


%files
%license
%doc man

%{_bindir}/crispy-doom
%{_bindir}/crispy-doom-setup
%{_bindir}/crispy-heretic
%{_bindir}/crispy-heretic-setup
%{_bindir}/crispy-hexen
%{_bindir}/crispy-hexen-setup
%{_bindir}/crispy-server
%{_bindir}/crispy-strife
%{_bindir}/crispy-strife-setup

%{_datadir}/applications/io.github.fabiangreffrath.Doom.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Heretic.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Hexen.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Setup.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Strife.desktop
%{_datadir}/applications/screensavers/io.github.fabiangreffrath.Doom_Screensaver.desktop

%{_datadir}/bash-completion/completions/crispy-doom
%{_datadir}/bash-completion/completions/crispy-heretic
%{_datadir}/bash-completion/completions/crispy-hexen
%{_datadir}/bash-completion/completions/crispy-strife
%{_datadir}/icons/hicolor/128x128/apps/crispy-doom.png

%{_datadir}/icons/hicolor/128x128/apps/crispy-heretic.png
%{_datadir}/icons/hicolor/128x128/apps/crispy-hexen.png
%{_datadir}/icons/hicolor/128x128/apps/crispy-setup.png
%{_datadir}/icons/hicolor/128x128/apps/crispy-strife.png

%{_datadir}/metainfo/io.github.fabiangreffrath.Doom.metainfo.xml
%{_datadir}/metainfo/io.github.fabiangreffrath.Heretic.metainfo.xml
%{_datadir}/metainfo/io.github.fabiangreffrath.Hexen.metainfo.xml
%{_datadir}/metainfo/io.github.fabiangreffrath.Strife.metainfo.xml

%{_mandir}/man5/crispy-doom.cfg.5.gz
%{_mandir}/man5/crispy-heretic.cfg.5.gz
%{_mandir}/man5/crispy-hexen.cfg.5.gz
%{_mandir}/man5/crispy-strife.cfg.5.gz
%{_mandir}/man5/default.cfg.5.gz
%{_mandir}/man5/heretic.cfg.5.gz
%{_mandir}/man5/hexen.cfg.5.gz
%{_mandir}/man5/strife.cfg.5.gz
%{_mandir}/man6/crispy-doom-setup.6.gz
%{_mandir}/man6/crispy-doom.6.gz
%{_mandir}/man6/crispy-heretic-setup.6.gz
%{_mandir}/man6/crispy-heretic.6.gz
%{_mandir}/man6/crispy-hexen-setup.6.gz
%{_mandir}/man6/crispy-hexen.6.gz
%{_mandir}/man6/crispy-server.6.gz
%{_mandir}/man6/crispy-strife-setup.6.gz
%{_mandir}/man6/crispy-strife.6.gz

%{_docdir}/crispy-doom/CMDLINE.doom
%{_docdir}/crispy-doom/COPYING.md
%{_docdir}/crispy-doom/ChangeLog
%{_docdir}/crispy-doom/INSTALL.doom
%{_docdir}/crispy-doom/NEWS.md
%{_docdir}/crispy-doom/NOT-BUGS.md
%{_docdir}/crispy-doom/PHILOSOPHY.md
%{_docdir}/crispy-doom/README.Music.md
%{_docdir}/crispy-doom/README.md
%{_docdir}/crispy-heretic/CMDLINE.heretic
%{_docdir}/crispy-heretic/INSTALL.heretic
%{_docdir}/crispy-hexen/CMDLINE.hexen
%{_docdir}/crispy-hexen/INSTALL.hexen
%{_docdir}/crispy-strife/CMDLINE.strife
%{_docdir}/crispy-strife/INSTALL.strife



%changelog
* Mon Jul 01 2024 bigleanator <98368716+bigleanator@users.noreply.github.com>
- Initial version
