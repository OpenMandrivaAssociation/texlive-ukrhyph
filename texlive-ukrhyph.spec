# revision 21081
# category Package
# catalog-ctan /language/hyphenation/ukrhyph
# catalog-date 2007-01-19 00:08:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ukrhyph
Version:	20070119
Release:	1
Summary:	Hyphenation Patterns for Ukrainian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/ukrhyph
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ukrhyph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ukrhyph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A range of patterns, depending on the encoding of the output
font (including the standard T2A, so one can use the patterns
with free fonts).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ukrhyph/catlcy.tex
%{_texmfdistdir}/tex/generic/ukrhyph/lcy2koi.tex
%{_texmfdistdir}/tex/generic/ukrhyph/lcy2lcy.tex
%{_texmfdistdir}/tex/generic/ukrhyph/lcy2ot2.tex
%{_texmfdistdir}/tex/generic/ukrhyph/lcy2t2a.tex
%{_texmfdistdir}/tex/generic/ukrhyph/lcy2ucy.tex
%{_texmfdistdir}/tex/generic/ukrhyph/rules60.tex
%{_texmfdistdir}/tex/generic/ukrhyph/rules90.tex
%{_texmfdistdir}/tex/generic/ukrhyph/rules_ph.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrenhyp.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhypfa.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.koi
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.lcy
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.ot2
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.t2a
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhyph.ucy
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhypmp.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhypmt.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhypsm.tex
%{_texmfdistdir}/tex/generic/ukrhyph/ukrhypst.tex
%doc %{_texmfdistdir}/doc/generic/ukrhyph/README
%doc %{_texmfdistdir}/doc/generic/ukrhyph/rules60.pdf
%doc %{_texmfdistdir}/doc/generic/ukrhyph/rules90.pdf
%doc %{_texmfdistdir}/doc/generic/ukrhyph/rules_ph.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}