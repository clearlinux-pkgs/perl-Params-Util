#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Util
Version  : 1.07
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Params-Util-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Params-Util-1.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-handle-util-perl/libio-handle-util-perl_0.01-2.debian.tar.xz
Summary  : Simple, compact and correct param-checking functions
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-Params-Util-lib = %{version}-%{release}
Requires: perl-Params-Util-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Params::Util - Simple, compact and correct param-checking functions
SYNOPSIS
# Import some functions
use Params::Util qw{_SCALAR _HASH _INSTANCE};

# If you are lazy, or need a lot of them...
use Params::Util ':ALL';

sub foo {
my $object  = _INSTANCE(shift, 'Foo') or return undef;
my $image   = _SCALAR(shift)          or return undef;
my $options = _HASH(shift)            or return undef;
# etc...
}

%package dev
Summary: dev components for the perl-Params-Util package.
Group: Development
Requires: perl-Params-Util-lib = %{version}-%{release}
Provides: perl-Params-Util-devel = %{version}-%{release}
Requires: perl-Params-Util = %{version}-%{release}

%description dev
dev components for the perl-Params-Util package.


%package lib
Summary: lib components for the perl-Params-Util package.
Group: Libraries
Requires: perl-Params-Util-license = %{version}-%{release}

%description lib
lib components for the perl-Params-Util package.


%package license
Summary: license components for the perl-Params-Util package.
Group: Default

%description license
license components for the perl-Params-Util package.


%prep
%setup -q -n Params-Util-1.07
cd ..
%setup -q -T -D -n Params-Util-1.07 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Params-Util-1.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Params-Util
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Params-Util/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Params-Util/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Params/Util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Params::Util.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Params/Util/Util.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Params-Util/LICENSE
/usr/share/package-licenses/perl-Params-Util/deblicense_copyright
