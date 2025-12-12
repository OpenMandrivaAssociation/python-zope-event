%define	pypi_name zope_event

Name:		python-zope-event
Summary:	Very basic event publishing system for Python
Version:	6.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
License:	ZPL-2.1
Group:		Development/Python
URL:		https://pypi.python.org/pypi/zope.event/
BuildSystem:  python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


%description
The zope.event package provides a simple event system, including:

- An event publishing API, intended for use by applications which are
  unaware of any subscribers to their events.
- A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

# Remove bundled egg-info
rm -rf src/zope.event.egg-info

%files
%doc README.rst
%license LICENSE.txt COPYRIGHT.txt
%{python_sitelib}/zope
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
