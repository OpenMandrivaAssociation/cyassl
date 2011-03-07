%define	major 0
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	SSL library developed for embedded environments
Name:		cyassl
Version:	1.9.0
Release:	%mkrel 1
License:	GPL
Group:		System/Libraries
URL:		http://www.yassl.com/
Source0:	http://www.yassl.com/%{name}-%{version}.zip
Patch0:		cyassl-1.4.0-malloc_linkage_fix.diff
BuildRequires:	dos2unix
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CyaSSL is a C language based SSL library developed for embedded environments
and real time operating systems where resources are constrained. CyaSSL is
about 10 times smaller than yaSSL and up to 20 times smaller than OpenSSL. User
benchmarking and feedback also reports dramatically better performance from
CyaSSL vs. OpenSSL in the vast majority of standard SSL operations.

%package -n	%{libname}
Summary:	Library associated with ncpfs
Group:		System/Libraries

%description -n	%{libname}
CyaSSL is a C language based SSL library developed for embedded environments
and real time operating systems where resources are constrained. CyaSSL is
about 10 times smaller than yaSSL and up to 20 times smaller than OpenSSL. User
benchmarking and feedback also reports dramatically better performance from
CyaSSL vs. OpenSSL in the vast majority of standard SSL operations.

%package -n	%{develname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
CyaSSL is a C language based SSL library developed for embedded environments
and real time operating systems where resources are constrained. CyaSSL is
about 10 times smaller than yaSSL and up to 20 times smaller than OpenSSL. User
benchmarking and feedback also reports dramatically better performance from
CyaSSL vs. OpenSSL in the vast majority of standard SSL operations.

%prep

%setup -q

find -type f -exec dos2unix -U {} \;
%patch0 -p1

%build
%serverbuild
%configure2_5x
%make

%install
rm -rf %{buildroot}

# the install is too borked...

%makeinstall_std -C src

install -d %{buildroot}%{_includedir}/cyassl/openssl
install -m0644 include/*.h %{buildroot}%{_includedir}/cyassl/
install -m0644 include/openssl/*.h %{buildroot}%{_includedir}/cyassl/openssl/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/cyassl
%dir %{_includedir}/cyassl/openssl
%{_includedir}/cyassl/*.h
%{_includedir}/cyassl/openssl/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.*a

