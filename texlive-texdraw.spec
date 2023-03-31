Name:		texlive-texdraw
Version:	64477
Release:	2
Summary:	Graphical macros, using embedded PostScript
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/texdraw
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdraw.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/texdraw
%doc %{_infodir}/texdraw.info*
%doc %{_texmfdistdir}/doc/support/texdraw

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
