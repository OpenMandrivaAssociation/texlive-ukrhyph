%global tl_name ukrhyph
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Hyphenation Patterns for Ukrainian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/ukrhyph
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ukrhyph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ukrhyph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A range of patterns, depending on the encoding of the output font
(including the standard T2A, so one can use the patterns with free
fonts).

