Summary:	A collection of useful classes and functions for Django
Name:		python-djblets
Version:	0.5.9
Release:	1
Group:		Applications/Networking
# Djblets is MIT licensed:
# http://code.google.com/p/reviewboard/wiki/Djblets
# Jquery is bundled in Djblets. Jquery is dual-licensed MIT or GPLv2, hence
# the package license is "MIT and (MIT or GPLv2)":
# https://www.redhat.com/archives/fedora-legal-list/2009-May/msg00025.html
License:	MIT and (MIT or GPL v2)
URL:		http://www.review-board.org/
Source0:	http://downloads.reviewboard.org/releases/Djblets/0.5/Djblets-%{version}.tar.gz
# Source0-md5:	389476bf51066392d769837ddb3068ef
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	sed >= 4.0
Requires:	python-PIL
Requires:	python-django >= 1.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of useful classes and functions for Django

%prep
%setup -q -n Djblets-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# Remove the "tests" subdirectory to avoid it polluting the main python
# namespace:
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%{py_sitescriptdir}/djblets
%{py_sitescriptdir}/Djblets*.egg-info
