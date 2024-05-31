#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : juk
Version  : 24.05.0
Release  : 46
URL      : https://download.kde.org/stable/release-service/24.05.0/src/juk-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/juk-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/juk-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: juk-bin = %{version}-%{release}
Requires: juk-data = %{version}-%{release}
Requires: juk-license = %{version}-%{release}
Requires: juk-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knotifications-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : phonon-dev
BuildRequires : qt6base-dev
BuildRequires : taglib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# A KDE Jukebox
<img src="https://apps.kde.org/app-icons/org.kde.juk.svg" align="right"
title="Juk logo" width="96" height="96">

%package bin
Summary: bin components for the juk package.
Group: Binaries
Requires: juk-data = %{version}-%{release}
Requires: juk-license = %{version}-%{release}

%description bin
bin components for the juk package.


%package data
Summary: data components for the juk package.
Group: Data

%description data
data components for the juk package.


%package doc
Summary: doc components for the juk package.
Group: Documentation

%description doc
doc components for the juk package.


%package license
Summary: license components for the juk package.
Group: Default

%description license
license components for the juk package.


%package locales
Summary: locales components for the juk package.
Group: Default

%description locales
locales components for the juk package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n juk-24.05.0
cd %{_builddir}/juk-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716524750
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716524750
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/juk
cp %{_builddir}/juk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/juk/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/juk-%{version}/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/juk/77976f406ba34009d9ba5a43b882fe6de68e5175 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang juk
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/juk
/usr/bin/juk

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.juk.desktop
/usr/share/dbus-1/interfaces/org.kde.juk.collection.xml
/usr/share/dbus-1/interfaces/org.kde.juk.player.xml
/usr/share/dbus-1/interfaces/org.kde.juk.search.xml
/usr/share/icons/hicolor/128x128/apps/juk.png
/usr/share/icons/hicolor/16x16/apps/juk.png
/usr/share/icons/hicolor/32x32/apps/juk.png
/usr/share/icons/hicolor/48x48/apps/juk.png
/usr/share/icons/hicolor/64x64/apps/juk.png
/usr/share/juk/pics/playing.png
/usr/share/juk/pics/theme.svg
/usr/share/kio/servicemenus/jukservicemenu.desktop
/usr/share/knotifications6/juk.notifyrc
/usr/share/metainfo/org.kde.juk.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/juk/history-playlist.png
/usr/share/doc/HTML/ca/juk/index.cache.bz2
/usr/share/doc/HTML/ca/juk/index.docbook
/usr/share/doc/HTML/ca/juk/normal-playlist.png
/usr/share/doc/HTML/ca/juk/search-playlist.png
/usr/share/doc/HTML/de/juk/history-playlist.png
/usr/share/doc/HTML/de/juk/index.cache.bz2
/usr/share/doc/HTML/de/juk/index.docbook
/usr/share/doc/HTML/de/juk/juk-adv-search.png
/usr/share/doc/HTML/de/juk/juk-file-renamer.png
/usr/share/doc/HTML/de/juk/juk-main.png
/usr/share/doc/HTML/de/juk/juk-tag-guesser.png
/usr/share/doc/HTML/de/juk/normal-playlist.png
/usr/share/doc/HTML/de/juk/search-playlist.png
/usr/share/doc/HTML/de/juk/toolbar.png
/usr/share/doc/HTML/en/juk/history-playlist.png
/usr/share/doc/HTML/en/juk/index.cache.bz2
/usr/share/doc/HTML/en/juk/index.docbook
/usr/share/doc/HTML/en/juk/juk-adv-search.png
/usr/share/doc/HTML/en/juk/juk-file-renamer.png
/usr/share/doc/HTML/en/juk/juk-main.png
/usr/share/doc/HTML/en/juk/juk-manage-folders.png
/usr/share/doc/HTML/en/juk/juk-tag-guesser.png
/usr/share/doc/HTML/en/juk/normal-playlist.png
/usr/share/doc/HTML/en/juk/search-playlist.png
/usr/share/doc/HTML/en/juk/toolbar.png
/usr/share/doc/HTML/es/juk/history-playlist.png
/usr/share/doc/HTML/es/juk/index.cache.bz2
/usr/share/doc/HTML/es/juk/index.docbook
/usr/share/doc/HTML/es/juk/juk-adv-search.png
/usr/share/doc/HTML/es/juk/juk-file-renamer.png
/usr/share/doc/HTML/es/juk/juk-main.png
/usr/share/doc/HTML/es/juk/juk-tag-guesser.png
/usr/share/doc/HTML/es/juk/normal-playlist.png
/usr/share/doc/HTML/es/juk/search-playlist.png
/usr/share/doc/HTML/es/juk/toolbar.png
/usr/share/doc/HTML/fr/juk/index.cache.bz2
/usr/share/doc/HTML/fr/juk/index.docbook
/usr/share/doc/HTML/it/juk/index.cache.bz2
/usr/share/doc/HTML/it/juk/index.docbook
/usr/share/doc/HTML/it/juk/juk-adv-search.png
/usr/share/doc/HTML/it/juk/juk-file-renamer.png
/usr/share/doc/HTML/it/juk/juk-main.png
/usr/share/doc/HTML/it/juk/juk-manage-folders.png
/usr/share/doc/HTML/it/juk/juk-tag-guesser.png
/usr/share/doc/HTML/it/juk/toolbar.png
/usr/share/doc/HTML/nl/juk/index.cache.bz2
/usr/share/doc/HTML/nl/juk/index.docbook
/usr/share/doc/HTML/nl/juk/juk-main.png
/usr/share/doc/HTML/sr/juk/index.cache.bz2
/usr/share/doc/HTML/sr/juk/index.docbook
/usr/share/doc/HTML/sr@latin/juk/index.cache.bz2
/usr/share/doc/HTML/sr@latin/juk/index.docbook
/usr/share/doc/HTML/uk/juk/index.cache.bz2
/usr/share/doc/HTML/uk/juk/index.docbook
/usr/share/doc/HTML/uk/juk/juk-adv-search.png
/usr/share/doc/HTML/uk/juk/juk-file-renamer.png
/usr/share/doc/HTML/uk/juk/juk-main.png
/usr/share/doc/HTML/uk/juk/juk-manage-folders.png
/usr/share/doc/HTML/uk/juk/juk-tag-guesser.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/juk/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/juk/77976f406ba34009d9ba5a43b882fe6de68e5175

%files locales -f juk.lang
%defattr(-,root,root,-)

