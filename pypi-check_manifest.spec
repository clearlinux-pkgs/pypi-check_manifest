#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-check_manifest
Version  : 0.48
Release  : 40
URL      : https://files.pythonhosted.org/packages/d6/22/b22e353f0ca0660c35e78975f0529a9e8241c22ca16480783fa237212b82/check-manifest-0.48.tar.gz
Source0  : https://files.pythonhosted.org/packages/d6/22/b22e353f0ca0660c35e78975f0529a9e8241c22ca16480783fa237212b82/check-manifest-0.48.tar.gz
Summary  : Check MANIFEST.in in a Python source package for completeness
Group    : Development/Tools
License  : MIT
Requires: pypi-check_manifest-bin = %{version}-%{release}
Requires: pypi-check_manifest-license = %{version}-%{release}
Requires: pypi-check_manifest-python = %{version}-%{release}
Requires: pypi-check_manifest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(build)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tomli)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
==============
        
        |buildstatus|_ |appveyor|_ |coverage|_
        
        Are you a Python developer?  Have you uploaded packages to the Python Package
        Index?  Have you accidentally uploaded *broken* packages with some files
        missing?  If so, check-manifest is for you.
        
        Quick start
        -----------

%package bin
Summary: bin components for the pypi-check_manifest package.
Group: Binaries
Requires: pypi-check_manifest-license = %{version}-%{release}

%description bin
bin components for the pypi-check_manifest package.


%package license
Summary: license components for the pypi-check_manifest package.
Group: Default

%description license
license components for the pypi-check_manifest package.


%package python
Summary: python components for the pypi-check_manifest package.
Group: Default
Requires: pypi-check_manifest-python3 = %{version}-%{release}

%description python
python components for the pypi-check_manifest package.


%package python3
Summary: python3 components for the pypi-check_manifest package.
Group: Default
Requires: python3-core
Provides: pypi(check_manifest)
Requires: pypi(build)
Requires: pypi(setuptools)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-check_manifest package.


%prep
%setup -q -n check-manifest-0.48
cd %{_builddir}/check-manifest-0.48
pushd ..
cp -a check-manifest-0.48 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656364719
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-check_manifest
cp %{_builddir}/check-manifest-0.48/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-check_manifest/b82514746d0268c7a2fca13e10d9d6daafa544c9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/check-manifest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-check_manifest/b82514746d0268c7a2fca13e10d9d6daafa544c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
