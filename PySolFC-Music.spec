Summary:	Music for PySolFC
Name:		PySolFC-Music
Version:	4.50
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/pysolfc/pysol-music-%{version}.tar.xz
# Source0-md5:	b71a138ce8e0d11c0a67359e980cce23
URL:		http://pysolfc.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	PySolFC
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the background music for PySolFC.

%prep
%setup -q -n pysol-music-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/PySolFC/

cp -a data/music $RPM_BUILD_ROOT%{_datadir}/PySolFC

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/PySolFC/music
