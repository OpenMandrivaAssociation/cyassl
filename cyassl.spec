%define	major 3
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	SSL library developed for embedded environments
Name:		cyassl
Version:	2.0.8
Release:	2
License:	GPL
Group:		System/Libraries
URL:		http://www.yassl.com/
Source0:	http://www.yassl.com/%{name}-%{version}.zip
BuildRequires:	autoconf automake m4 libtool
BuildRequires:	dos2unix

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

find -type f -exec dos2unix {} \;

%build
rm -f configure
autoreconf -fi

%serverbuild
%configure2_5x \
    --enable-shared \
    --disable-static \
    --enable-dtls \
    --enable-opensslExtra \
    --enable-ipv6 \
    --enable-fortress \
    --enable-bump \
    --enable-fasthugemath \
    --enable-hugecache \
    --enable-aesni \
    --enable-ripemd \
    --enable-sha512 \
    --enable-sessioncerts \
    --enable-keygen \
    --enable-certgen \
    --enable-hc128 \
    --enable-psk

%make

%install

%makeinstall_std

# cleanups
rm -rf %{buildroot}%{_sysconfdir}/ssl
rm -f %{buildroot}%{_libdir}/lib*.*a
rm -rf %{buildroot}%{_datadir}/doc

%files -n %{libname}
%doc README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc examples/echoclient/echoclient.c
%doc examples/echoserver/echoserver.c
%doc examples/server/server.c
%dir %{_includedir}/cyassl
%dir %{_includedir}/cyassl/ctaocrypt
%dir %{_includedir}/cyassl/openssl
%{_includedir}/cyassl/*.h
%{_includedir}/cyassl/ctaocrypt/*.h
%{_includedir}/cyassl/openssl/*.h
%{_libdir}/lib*.so
