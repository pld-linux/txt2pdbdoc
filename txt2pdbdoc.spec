Summary:	Converts Text or HTML to PalmPilots's PDB/DOC file format
Summary(pl):	Konwerter tekstu i HTML na format PalmPilotów - PDB/DOC
Name:		txt2pdbdoc
Version:	1.2.1
Release:	5
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://shell3.ba.best.com/pub/pjl/software/%{name}-%{version}.tar.gz
URL:		http://www.best.com/~pjl/software.html
Patch0:		%{name}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts text or HTML files to PalmPilot's E-Book/DOC file, or
vice-versa.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,4}}

install html2pdbtxt pdbtxt2html $RPM_BUILD_ROOT%{_bindir}
install txt2pdbdoc $RPM_BUILD_ROOT%{_bindir}

install man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man4/*.4 $RPM_BUILD_ROOT%{_mandir}/man4

gzip -9nf AUTHORS Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[14]/*
