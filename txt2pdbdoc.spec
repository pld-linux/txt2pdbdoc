Name: txt2pdbdoc
Summary: Converts Text or HTML to PalmPilots's PDB/DOC file format
Version: 1.2.1
Release: 1
Source: ftp://shell3.ba.best.com/pub/pjl/software/txt2pdbdoc-1.2.1.tar.gz
URL: http://www.best.com/~pjl/software.html
Patch: txt2pdbdoc.diff
Group: Applications/Productivity
Packager: Avi Alkalay <avi@br.ibm.com>
Prefix: /usr
Copyright: GPL
BuildRoot: /var/tmp/txt2pdbdoc

%description
Converts text or HTML files to PalmPilot's E-Book/DOC file, or vice-versa.

%prep
%setup
%patch -p1
%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/man/man1 $RPM_BUILD_ROOT/usr/man/man4
strip txt2pdbdoc
#make -n install
cp html2pdbtxt $RPM_BUILD_ROOT/usr/bin
cp pdbtxt2html $RPM_BUILD_ROOT/usr/bin
cp txt2pdbdoc $RPM_BUILD_ROOT/usr/bin
cp man/man1/*.1 $RPM_BUILD_ROOT/usr/man/man1
cp man/man4/*.4 $RPM_BUILD_ROOT/usr/man/man4


%clean
make clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/html2pdbtxt
/usr/bin/pdbtxt2html
/usr/bin/txt2pdbdoc
%doc /usr/man/man1/*
%doc /usr/man/man4/*
%doc AUTHORS COPYING Changes INSTALL README
