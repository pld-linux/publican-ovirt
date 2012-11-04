Summary:	Publican documentation template files for oVirt
Summary(pl.UTF-8):	Pliki szablonów dokumentacji Publicana dla projektu oVirt
Name:		publican-ovirt
Version:	1.3
Release:	1
License:	Open Publication
Group:		Development/Tools
Source0:	https://fedorahosted.org/releases/p/u/publican/%{name}-%{version}.tgz
# Source0-md5:	e9b6ff73da8cf6f65acda1e651bef8c3
URL:		https://publican.fedorahosted.org/
BuildRequires:	publican >= 2.0
Requires:	publican >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides common files and templates needed to build
documentation for oVirt with Publican.

%description -l pl.UTF-8
Ten pakiet udostępnia wspólne pliki oraz szablony wymagane do
budowania dokumentacji dla projektu oVirt przy użyciu Publicana.

%prep
%setup -q

%build
publican build --formats=xml --langs=all --publish

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

publican install_brand --path=$RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/publican/Common_Content/oVirt
