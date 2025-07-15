Summary:	Converts Text or HTML to PalmPilot's PDB/DOC file format
Summary(pl.UTF-8):	Konwerter tekstu i HTML na format PalmPilotów - PDB/DOC
Name:		txt2pdbdoc
Version:	1.2.1
Release:	6
License:	GPL
Group:		Applications/Text
Source0:	ftp://shell3.ba.best.com/pub/pjl/software/%{name}-%{version}.tar.gz
# Source0-md5:	76768cbb5dcc06b4bcf90226d96ca618
URL:		http://www.best.com/~pjl/software.html
Patch0:		%{name}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts text or HTML files to PalmPilot's E-Book/DOC file, or
vice-versa.

%description -l pl.UTF-8
Konwerter plików tekstowych i HTML na pliki E-Book/DOC PalmPilotów i
odwrotnie.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,4}}

install html2pdbtxt pdbtxt2html $RPM_BUILD_ROOT%{_bindir}
install txt2pdbdoc $RPM_BUILD_ROOT%{_bindir}

install man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man4/*.4 $RPM_BUILD_ROOT%{_mandir}/man4


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[14]/*
