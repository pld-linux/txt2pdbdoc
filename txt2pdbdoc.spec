Summary:	Converts Text or HTML to PalmPilots's PDB/DOC file format
Name:		txt2pdbdoc
Version:	1.2.1
Release:	2
Copyright:	GPL
Group:		Applications/Productivity
Source:		ftp://shell3.ba.best.com/pub/pjl/software/%{name}-%{version}.tar.gz
URL:		http://www.best.com/~pjl/software.html
Patch:		txt2pdbdoc.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Converts text or HTML files to PalmPilot's E-Book/DOC file, or vice-versa.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/man/man{1,4}}
install html2pdbtxt pdbtxt2html $RPM_BUILD_ROOT/usr/bin
install -s txt2pdbdoc $RPM_BUILD_ROOT/usr/bin

cp pdbtxt2html $RPM_BUILD_ROOT/usr/bin
cp txt2pdbdoc $RPM_BUILD_ROOT/usr/bin

install man/man1/*.1 $RPM_BUILD_ROOT/usr/share/man/man1
install man/man4/*.4 $RPM_BUILD_ROOT/usr/share/man/man4

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man?/* \
	AUTHORS Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
/usr/share/man/man[14]/*

%changelog
* Tue May 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.1-2]
- rewrited to PLD coding style,
- now package is FHS 2.0 compiliat.

* Tue Dec 15 1998 Avi Alkalay <avi@br.ibm.com>
- first release in rpm package.
