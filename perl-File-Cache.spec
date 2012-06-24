%include	/usr/lib/rpm/macros.perl
Summary:	File-Cache perl module
Summary(pl):	Modu� perla File-Cache
Name:		perl-File-Cache
Version:	0.16
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Cache-%{version}.tar.gz
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
%setup -q -n File-Cache-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/Cache.pm
