# revision 31894
# category Package
# catalog-ctan /graphics/texdraw
# catalog-date 2012-06-05 21:37:17 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-texdraw
Version:	20170414
Release:	1
Summary:	Graphical macros, using embedded PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/texdraw
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXdraw is a set of macro definitions for TeX, which allow the
user to produce PostScript drawings from within TeX and LaTeX.
TeXdraw has been designed to be extensible. Drawing 'segments'
are relocatable, self-contained units. Using a combination of
the TeX's grouping mechanism and the gsave/grestore mechanism
in PostScript, drawing segments allow for local changes to the
scaling and line parameters. Using TeX's macro definition
capability, new drawing commands can be constructed from
drawing segments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/texdraw/blockdiagram.tex
%{_texmfdistdir}/tex/generic/texdraw/texdraw.sty
%{_texmfdistdir}/tex/generic/texdraw/texdraw.tex
%{_texmfdistdir}/tex/generic/texdraw/txdexamp.latex
%{_texmfdistdir}/tex/generic/texdraw/txdexamp.tex
%{_texmfdistdir}/tex/generic/texdraw/txdps.tex
%{_texmfdistdir}/tex/generic/texdraw/txdtools.tex
%doc %{_infodir}/texdraw.info*
%doc %{_texmfdistdir}/doc/support/texdraw/ChangeLog
%doc %{_texmfdistdir}/doc/support/texdraw/README
%doc %{_texmfdistdir}/doc/support/texdraw/texdraw.cps
%doc %{_texmfdistdir}/doc/support/texdraw/texdraw.fns
%doc %{_texmfdistdir}/doc/support/texdraw/texdraw.ps
%doc %{_texmfdistdir}/doc/support/texdraw/texdraw.texi
%doc %{_texmfdistdir}/doc/support/texdraw/txi-src.tgz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
