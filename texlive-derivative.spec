Name:		texlive-derivative
Version:	63850
Release:	1
Summary:	Nice and easy derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/derivative
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/derivative.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/derivative.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typesetting derivatives and differentials in a consistent way
are clumsy and require care to ensure the preferred formatting.
Several packages have been developed for this purpose, each
with its own features and drawbacks, with the most ambitious
one being diffcoeff. While this package is comparable to
diffcoeff in terms of features, it takes a different approach.
One difference is this package provides more options to tweak
the format of the derivatives and differentials. However, the
automatic calculation of the total order isn't as developed as
the one in diffcoeff. This package makes it easy to write
derivatives and differentials consistently with its predefined
commands. It also provides a set of commands that can define
custom derivatives and differential operators. The options
follow a consistent naming scheme making them easy to use and
understand.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/derivative
%doc %{_texmfdistdir}/doc/latex/derivative

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
