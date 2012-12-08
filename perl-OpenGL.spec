%define upstream_name    OpenGL
%define upstream_version 0.66

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to OpenGL drawing/imaging library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		perl-OpenGL-0.62-dist.patch
BuildRequires: mesa-common-devel
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(glut)
BuildRequires: perl-devel


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
%patch0 -p0 -b .dist
# test.pl requires interaction, prefer using tests in t/
rm test.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor dist=NO_EXCLUSIONS
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
%{make}

# since we're building without exclusion, test fail
#%check
#%{make} test

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


%changelog
* Mon Jan 23 2012 Oden Eriksson <oeriksson@mandriva.com> 0.660.0-1mdv2012.0
+ Revision: 766821
- 0.66
- rediffed P0
- try to fix deps
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.640.0-2
+ Revision: 667284
- mass rebuild

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 596632
- update to 0.64

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.630.0-4mdv2011.0
+ Revision: 564571
- rebuild for perl 5.12.1

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 0.630.0-3mdv2011.0
+ Revision: 556761
- add fedora patch to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - disable testsuite as it failed with: "GLUT: Fatal Error in glversion: OpenGL
      GLX extension not supported by display: :99

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.630.0-1mdv2011.0
+ Revision: 552484
- update to 0.63

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.620.0-1mdv2010.1
+ Revision: 483045
- update to 0.62

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2010.1
+ Revision: 463974
- update to 0.61

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.1
+ Revision: 461677
- skipping tests
- even with dist=NO_EXCLUSIONS set, it needs a virtual framebuffer
- build module without any gl exclusion
- adding missing buildrequires:
- running under a x server for makefile to probe stuff
- import perl-OpenGL


* Fri Nov 06 2009 cpan2dist 0.60-1mdv
- initial mdv release, generated with cpan2dist
