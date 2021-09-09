#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Exact
Version  : 3.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/Exact_3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Exact_3.0.tar.gz
Summary  : Unconditional Exact Test
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rootSolve
BuildRequires : R-rootSolve
BuildRequires : buildreq-R

%description
For comparing two independent proportions, performs Barnard's test (1945)

%prep
%setup -q -c -n Exact
cd %{_builddir}/Exact

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631210752

%install
export SOURCE_DATE_EPOCH=1631210752
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Exact
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Exact
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Exact
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Exact || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Exact/DESCRIPTION
/usr/lib64/R/library/Exact/INDEX
/usr/lib64/R/library/Exact/Meta/Rd.rds
/usr/lib64/R/library/Exact/Meta/features.rds
/usr/lib64/R/library/Exact/Meta/hsearch.rds
/usr/lib64/R/library/Exact/Meta/links.rds
/usr/lib64/R/library/Exact/Meta/nsInfo.rds
/usr/lib64/R/library/Exact/Meta/package.rds
/usr/lib64/R/library/Exact/NAMESPACE
/usr/lib64/R/library/Exact/NEWS.Rd
/usr/lib64/R/library/Exact/R/Exact
/usr/lib64/R/library/Exact/R/Exact.rdb
/usr/lib64/R/library/Exact/R/Exact.rdx
/usr/lib64/R/library/Exact/help/AnIndex
/usr/lib64/R/library/Exact/help/Exact.rdb
/usr/lib64/R/library/Exact/help/Exact.rdx
/usr/lib64/R/library/Exact/help/aliases.rds
/usr/lib64/R/library/Exact/help/paths.rds
/usr/lib64/R/library/Exact/html/00Index.html
/usr/lib64/R/library/Exact/html/R.css
