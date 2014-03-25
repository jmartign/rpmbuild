%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define whisper_version 0.9.12
%define ok_version 02
%define whisper_revision 1d99a3be4f5b147c0a96419911743e3fb4696bfa

Name:           ok-whisper
Version:        %{whisper_version}
Release:        %{ok_version}+%{whisper_revision}
Summary:        Fixed size round-robin style database
Group:          Applications/Databases
License:        Apache Software License 2.0
URL:            https://launchpad.net/graphite
Vendor:         Chris Davis <chrismd@gmail.com>
Packager:       Dan Carley <dan.carley@gmail.com>

Source0:        whisper-0.9.x-%{whisper_revision}.tar.gz
Patch0:         whisper-compat.patch

BuildArch:      noarch

BuildRequires:  python python-devel python-setuptools
Requires:       python

%description
Whisper is a fixed-size database, similar in design to RRD.  It provides fast,
reliable storage of numeric data over time.

%prep
%setup -q -n whisper-0.9.x
%patch0 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} -c 'import setuptools; execfile("setup.py")' build

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE

%{python_sitelib}/*
/usr/bin/*

%changelog
* Tue Mar 25 2014 Oleksiy Kovyrin <alexey@kovyrin.net> - 0.9.12-1
- Port a6e2176eb624f0c09df399b4f8464a5a08789bd6 to 0.9.x to make new graphite-web compatible with this package.

* Tue Mar 25 2014 Oleksiy Kovyrin <alexey@kovyrin.net> - 0.9.12-1
- New upstream version.

* Fri Jun 1 2012 Ben P <ben@g.megatron.org> - 0.9.10-1
- New upstream version.

* Sat Oct 8 2011 Dan Carley <dan.carley@gmail.com> - 0.9.9-1
- New upstream version.

* Mon May 23 2011 Dan Carley <dan.carley@gmail.com> - 0.9.8-2
- Repackage with minor changes.

* Tue Apr 20 2011 Chris Abernethy <cabernet@chrisabernethy.com> - 0.9.8-1
- Update source to upstream v0.9.8
- Minor updates to spec file

* Thu Mar 17 2011 Daniel Aharon <daharon@sazze.com> - 0.9.7-1
- Add dependencies and description.
