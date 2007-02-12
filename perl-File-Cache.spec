#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Cache
Summary:	File::Cache - share data between processes via filesystem
Summary(pl.UTF-8):   File::Cache - uwspólnianie danych pomiędzy procesami poprzez system plików
Name:		perl-File-Cache
Version:	0.16
Release:	8
License:	GPL v1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	712371ae4ee88de11072d1616ae0af72
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Cache implements an object store where data is persisted across
processes in the filesystem. It was written to compliment IPC::Cache.

Where IPC::Cache is faster for small numbers of simple objects,
File::Cache tends toward being more performant when caching large
numbers of complex objects.

%description -l pl.UTF-8
File::Cache implementuje obiekt przechowujący dane, które są
zachowywane na czas działań w systemie plików. Został napisany jako
odpowiednik IPC::Cache.

O ile IPC::Cache jest szybszy dla małych ilości prostych obiektów,
File::Cache próbuje być bardziej wydajny przy cachowaniu większych
ilości złożonych obiektów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES
%{perl_vendorlib}/File/Cache.pm
