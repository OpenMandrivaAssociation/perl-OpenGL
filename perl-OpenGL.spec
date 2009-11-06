%define upstream_name    OpenGL
%define upstream_version 0.60

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to OpenGL drawing/imaging library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: x11-server-xvfb

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}
# test.pl requires interaction, prefer using tests in t/
rm test.pl

%build
xvfb-run %{__perl} Makefile.PL INSTALLDIRS=vendor
%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README GIT_CHANGES
%{_mandir}/man3/*
%perl_vendorlib/*
