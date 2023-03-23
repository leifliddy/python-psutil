%global srcname psutil

%global _desc \
psutil is a module providing an interface for retrieving information on all \
running processes and system utilization (CPU, memory, disks, network, users) in \
a portable way by using Python, implementing many functionalities offered by \
command line tools such as: ps, top, df, kill, free, lsof, free, netstat, \
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.

%global _sum A process and system utilities module for Python

# xxx
%global python3_pkgversion 36

Name:           python-psutil
Version:        5.6.7
Release:        1%{?dist}
Summary:        %{_sum}

Group:          Development/Languages
License:        BSD
URL:            https://github.com/giampaolo/psutil
Source0:        https://github.com/giampaolo/psutil/archive/release-%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel

%description
%{_desc}


%package -n python%{python3_pkgversion}-psutil
Summary:        %{_sum}
Group:          Development/Languages
%{?python_provide:%python_provide python%{python3_pkgversion}-psutil}

%description -n python%{python3_pkgversion}-psutil
%{_desc}


%prep
%autosetup -p1 -n %{srcname}-release-%{version}

# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-psutil
%license LICENSE
%doc CREDITS HISTORY.rst README.rst
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/%{srcname}/*.so


%changelog
* Sun Feb 16 2020 Kevin Fenzi <kevin@scrye.com> - 5.6.7-1
- Update to 5.6.7. Fixes CVE-2019-18874

* Sat May 04 2019 Kevin Fenzi <kevin@scrye.com> - 2.2.1-6
- Clean up spec and source/upstream.

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 2.2.1-5
- Rebuilt to change main python from 3.4 to 3.6

* Mon Nov 12 2018 Orion Poplawski <orion@nwra.com> - 2.2.1-4
- Build for python36

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.1-3
- Use proper Python3 macros

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 2.2.1-2
- Build a package for Python34

* Wed Dec 09 2015 Ralph Bean <rbean@redhat.com> - 2.2.1-1
- Update to 2.2.1 for https://bugzilla.redhat.com/1288221
- Update names of %%doc files.

* Wed Mar 11 2015 Alan Pevec <apevec@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Tue Feb 18 2014 Matthias Runge <mrunge@redhat.com> - 0.6.1-3
- epel doesn't have python3


* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Mohamed El Morabity <melmorabity@fedorapeople.org> - 0.6.1-1
- Update to 0.6.1

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.5.1-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sun Nov 20 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Mon Jul 18 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Mar 23 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Spec cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-4
- bump, because previous build nvr already existed in F-14

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-2
- Add missing popd in %%build

* Sat Mar 27 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-1
- Update to 0.1.3
- Remove useless call to 2to3 and corresponding BuildRequires
  python2-tools (this version supports Python 3)

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-4
- Change python-utils BuildRequires for python2-utils

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-3
- Add python3 subpackage

* Thu Jan 14 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-2
- Drop no-shebang patch for a sed command
- Drop test suite from %%doc tag

* Fri Jan  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-1
- Initial RPM release
