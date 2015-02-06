%define	tarname zope.event
%define	rel	1
%if %mdkversion < 201100
%else
%endif

Summary:	Very basic event publishing system for Python

Name:		python-zope-event
Version:	4.0.3
Release:	2
Source0:	http://pypi.python.org/packages/source/z/zope.event/zope.event-%{version}.tar.gz
License:	ZPL
Group:		Development/Python
Url:		http://pypi.python.org/pypi/zope.event/
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
The zope.event package provides a simple event system, including:

- An event publishing API, intended for use by applications which are
  unaware of any subscribers to their events.
- A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc *.txt
%{py_puresitedir}/zope*



