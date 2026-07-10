%global tl_name derivative
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Nice and easy derivatives
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/derivative
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/derivative.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/derivative.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typesetting derivatives and differentials in a consistent way are clumsy
and require care to ensure the preferred formatting. Several packages
have been developed for this purpose, each with its own features and
drawbacks, with the most ambitious one being diffcoeff. While this
package is comparable to diffcoeff in terms of features, it takes a
different approach. One difference is this package provides more options
to tweak the format of the derivatives and differentials. However, the
automatic calculation of the total order isn't as developed as the one
in diffcoeff. This package makes it easy to write derivatives and
differentials consistently with its predefined commands. It also
provides a set of commands that can define custom derivatives and
differential operators. The options follow a consistent naming scheme
making them easy to use and understand.

