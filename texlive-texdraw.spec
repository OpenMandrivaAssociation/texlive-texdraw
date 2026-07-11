%global tl_name texdraw
%global tl_revision 64477

Name:		texlive-%{tl_name}
Epoch:		1
Version:	v2r3
Release:	%{tl_revision}.1
Summary:	Graphical macros, using embedded PostScript
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/texdraw
License:	cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeXdraw is a set of macro definitions for TeX, which allow the user to
produce PostScript drawings from within TeX and LaTeX. TeXdraw has been
designed to be extensible. Drawing 'segments' are relocatable, self-
contained units. Using a combination of TeX's grouping mechanism and the
gsave/grestore mechanism in PostScript, drawing segments allow for local
changes to the scaling and line parameters. Using TeX's macro definition
capability, new drawing commands can be constructed from drawing
segments.

