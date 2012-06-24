%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Cache
Summary:	File::Cache perl module
Summary(pl):	Modu� perla File::Cache
Name:		perl-File-Cache
Version:	0.16
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Cache implements an object store where data is persisted across
processes in the filesystem. It was written to compliment IPC::Cache.

Where IPC::Cache is faster for small numbers of simple objects,
File::Cache tends toward being more performant when caching large
numbers of complex objects.

%description -l pl
File::Cache implementuje obiekt przechowuj�cy dane, kt�re s�
zachowywane na czas dzia�a� w systemie plik�w. Zosta� napisany jako
odpowiednik IPC::Cache.

O ile IPC::Cache jest szybszy dla ma�ych ilo�ci prostych obiekt�w,
File::Cache pr�buje by� bardziej wydajny przy cachowaniu wi�kszych
ilo�ci z�o�onych obiekt�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO CHANGES
%{perl_sitelib}/File/Cache.pm
