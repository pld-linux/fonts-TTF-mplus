Summary:	M+ fonts (Latin and Japanese)
Summary(pl.UTF-8):	Fonty M+ (łacińskie i japońskie)
Name:		fonts-TTF-mplus
Version:	056
Release:	0.TESTFLIGHT.1
License:	mplus (distributable)
Group:		Fonts
#Source0Download: http://sourceforge.jp/projects/mplus-fonts/releases/
Source0:	http://dl.sourceforge.jp/mplus-fonts/6650/mplus-TESTFLIGHT-%{version}.tar.xz
# Source0-md5:	1ad9f99b52122d0239b55aac4c194881
URL:		http://mplus-fonts.sourceforge.jp/mplus-outline-fonts/index-en.html
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
M+ fonts: proportional Latin (4 variations), fixed-halfwidth Latin (3
variations), fixed-fullwidth Japanese (2 Kana variations). 7 weights
from Thin to Black are included, but fixed-halfwidth Latin with 5
weights from Thin to Bold.

%description -l pl.UTF-8
Fonty M+: łacińskie proporcjonalne (4 warianty), łacińskie o stałej
szerokości połówkowej (3 warianty), japońskie o stałej pełnej
szerokości (2 warianty Kana). Dostępne jest 7 grubości fontów, z
wyjątkiem łacińskich o stałej szerokości połówkowej, których jest 5
grubości.

%prep
%setup -q -n mplus-TESTFLIGHT-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README_E LICENSE_E
%lang(ja) %doc README_J LICENSE_J
%{_ttffontsdir}/mplus-*.ttf
