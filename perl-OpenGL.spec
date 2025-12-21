%define modname	OpenGL
%define modver	0.70

Summary:	Interface to OpenGL drawing/imaging library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHM/%{modname}-%{modver}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/perl-OpenGL/raw/master/f/0001-Don-t-check-current-display-for-extensions.patch
BuildRequires:	make
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	perl-devel

%description
Naming convention:
    Virtually all of the OpenGL 1.0, and 1.1 functions are available, and
    most of 1.2. In general, the calling sequence is identical in Perl as
    in C.

    Most functions that have no pointer arguments are called identically in
    Perl as in C, and the same name is used.

    Functions that use Perl array arguments and have been changed in "the
    obvious way" -- to take a variable number of arguments and/or to return
    an array -- have the the same names as their C counterparts, but with a
    _p suffix.

%prep
%setup -qn %{modname}-%{modver}
%autopatch -p1
# test.pl requires interaction, prefer using tests in t/
rm test.pl

%build
sed -i -e 's#L/usr/lib#L%{_libdir}#g' Makefile.PL
perl Makefile.PL INSTALLDIRS=vendor dist=NO_EXCLUSIONS
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
%make_build

%check
# since we're building without exclusion, test fail
#make test

%install
%make_install

%files
%doc CHANGES README
%{perl_vendorarch}/*
%{_mandir}/man3/*
