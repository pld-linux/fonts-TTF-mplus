Summary:	M+ fonts
Name:		fonts-TTF-mplus
Version:	031
Release:	0.TESTFLIGHT.1
License:	mplus (distributable)
Group:		Fonts
Source0:	http://dl.sourceforge.jp/mplus-fonts/6650/mplus-TESTFLIGHT-%{version}.tar.gz
# Source0-md5:	5bc303ddc3bb04ab9713146eef584663
URL:		http://mplus-fonts.sourceforge.jp/mplus-outline-fonts/index-en.html
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
M+ fonts

%prep
%setup -q -n mplus-TESTFLIGHT-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

cp -a *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README_E README_J LICENSE_E LICENSE_J
%{_ttffontsdir}/mplus-*.ttf
