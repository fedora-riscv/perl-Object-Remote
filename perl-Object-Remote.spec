Name:           perl-Object-Remote
Version:        0.003006
Release:        1%{?dist}
Summary:        Call methods on objects in other processes or on other hosts
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Object-Remote/
Source0:        http://www.cpan.org/authors/id/M/MS/MSTROUT/Object-Remote-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::C3)
# Class::C3::next - the part of perl-Class-C3, but it isn't listed in provides
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Declare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Future) >= 0.29
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Contextual) >= 0.005
BuildRequires:  perl(Log::Contextual::Role::Router)
BuildRequires:  perl(Method::Generate::BuildAll)
BuildRequires:  perl(Method::Generate::DemolishAll)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::HandleMoose::_TypeMap)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 1
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Algorithm::C3)
Requires:       perl(Class::C3)
Requires:       perl(Future) >= 0.29
Requires:       perl(Log::Contextual) >= 0.005
Requires:       perl(Log::Contextual::Role::Router)
Requires:       perl(Method::Generate::BuildAll)
Requires:       perl(Method::Generate::DemolishAll)
Requires:       perl(Moo) >= 1.006
Requires:       perl(Moo::HandleMoose::_TypeMap)
Requires:       perl(MRO::Compat)
Requires:       openssh-clients
Requires:       sudo

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Future\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(maybe\\)$
%global __provides_exclude %__provides_exclude|^perl\\(maybe::start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(start\\)$
%global __provides_exclude %__provides_exclude|^perl\\(then\\)$

%description
Object::Remote allows you to create an object in another process - usually
one running on another machine you can connect to via ssh, although there
are other connection mechanisms available.

%prep
%setup -q -n Object-Remote-%{version}
sed -i -e '1s|#!/usr/bin/env perl|#!perl|' bin/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jan 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003006-1
- 0.003006 bump

* Thu Jan 07 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-2
- Update list of dependencies

* Wed Dec 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.003005-1
- Initial release
