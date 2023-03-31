Name: x11-font-bh-lucidatypewriter-75dpi
Version: 1.0.4
Release: 2
Summary: Xorg X11 font bh-lucidatypewriter-75dpi
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-bh-lucidatypewriter-75dpi-%{version}.tar.xz
# See #38627 for licensing
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font bh-lucidatypewriter-75dpi.

%prep
%autosetup -p1 -n font-bh-lucidatypewriter-75dpi-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/75dpi
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.scale

%post
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%postun
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%files
%doc COPYING
%{_datadir}/fonts/75dpi/lut*
