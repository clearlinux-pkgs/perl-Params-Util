#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Util
Version  : 1.07
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Params-Util-1.07.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Params-Util-1.07.tar.gz
Summary  : 'Simple, compact and correct param-checking functions'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Params-Util-lib
Requires: perl-Params-Util-doc

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

%package doc
Summary: doc components for the perl-Params-Util package.
Group: Documentation

%description doc
doc components for the perl-Params-Util package.


%package lib
Summary: lib components for the perl-Params-Util package.
Group: Libraries

%description lib
lib components for the perl-Params-Util package.


%prep
%setup -q -n Params-Util-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/Util.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Params/Util/Util.so
