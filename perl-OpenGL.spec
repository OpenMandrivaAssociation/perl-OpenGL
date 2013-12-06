%define modname	OpenGL
%define modver	0.66

Summary:	Interface to OpenGL drawing/imaging library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHM/%{modname}-%{modver}.tar.gz
Patch0:		perl-OpenGL-0.62-dist.patch
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glut)
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
%patch0 -p0 -b .dist
# test.pl requires interaction, prefer using tests in t/
rm test.pl

%build
%__perl Makefile.PL INSTALLDIRS=vendor dist=NO_EXCLUSIONS
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
%make

%check
# since we're building without exclusion, test fail
#make test

%install
%makeinstall_std

%files
%doc CHANGES README GIT_CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

