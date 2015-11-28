# TODO
# - use system jquery, jquery-ui
Summary:	A collection of useful classes and functions for Django
Name:		python-djblets
Version:	0.7.10
Release:	2
Group:		Applications/Networking
# Djblets is MIT licensed:
# http://code.google.com/p/reviewboard/wiki/Djblets
# jQuery is bundled in Djblets. Jquery is dual-licensed MIT or GPLv2, hence
# the package license is "MIT and (MIT or GPLv2)":
# https://www.redhat.com/archives/fedora-legal-list/2009-May/msg00025.html
License:	MIT and (MIT or GPL v2)
URL:		http://www.review-board.org/
Source0:	http://downloads.review-board.org/releases/Djblets/0.7/Djblets-%{version}.tar.gz
# Source0-md5:	c2e1987fc6badad138743aa0ea009922
BuildRequires:	fslint
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-django-pipeline >= 1.2.24
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	python-PIL
Requires:	python-django >= 1.4.2
Requires:	python-django-pipeline >= 1.2.24
Requires:	python-feedparser >= 5.1.2
Requires:	python-pytz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of useful classes and functions for Django

%prep
%setup -q -n Djblets-%{version}

# Remove packaged egg-info so it's regenerated by setup.py
%{__rm} -r Djblets*.egg-info

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

# hardlink files with fingerprinted variants
findup -m $RPM_BUILD_ROOT

# Remove the "tests" subdirectory to avoid it polluting the main python namespace:
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{py_sitescriptdir}/djblets
%{py_sitescriptdir}/Djblets*.egg-info
