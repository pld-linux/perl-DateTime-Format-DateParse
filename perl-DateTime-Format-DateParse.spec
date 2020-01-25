#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	DateTime
%define		pnam	Format-DateParse
Summary:	DateTime::Format::DateParse - Parses Date::Parse compatible formats
Summary(pl.UTF-8):	DateTime::Format::DateParse - analiza formatów kompatybilnych z Date::Parse
Name:		perl-DateTime-Format-DateParse
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9a66f74aeba7c45730430dbf9b37cfd
URL:		http://search.cpan.org/dist/DateTime-Format-DateParse/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 0.29
BuildRequires:	perl-DateTime-TimeZone >= 0.27
BuildRequires:	perl-TimeDate >= 2.27
%endif
Requires:	perl-DateTime >= 0.29
Requires:	perl-DateTime-TimeZone >= 0.27
Requires:	perl-TimeDate >= 2.27
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a compatibility wrapper around Date::Parse.

%description -l pl.UTF-8
Ten moduł jest obudowaniem dla kompatybilności z Date::Parse.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/Format/DateParse.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DateTime/Format/DateParse.pm
%{_mandir}/man3/DateTime::Format::DateParse.3pm*
