%define	tarname zope.event
%define name	python-zope-event
%define version 4.0.0
%define	rel	1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Very basic event publishing system for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/z/%{tarname}/%{tarname}-%{version}.tar.gz
License:	ZPL
Group:		Development/Python
Url:		http://pypi.python.org/pypi/zope.event/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%py_sitedir/zope*


%changelog
* Wed Jun 20 2012 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 806505
- imported package python-zope-event

