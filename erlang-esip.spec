%global srcname esip


Name: erlang-%{srcname}
Version: 1.0.8
Release: %mkrel 2

Group:   Development/Erlang

License: ASL 2.0
Summary: ProcessOne SIP server component in Erlang
URL: https://github.com/processone/esip/
Source0: https://github.com/processone/%{srcname}/archive/%{version}.tar.gz
# Patch an 'include' statement to search the system libraries rather than
# its deps directory.
Patch0: include_lib.patch

Provides:  erlang-p1_sip = %{version}-%{release}
Obsoletes: erlang-p1_sip < 1.0.2

BuildRequires: erlang-rebar
BuildRequires: erlang-fast_tls >= 1.0.7
BuildRequires: erlang-stun >= 1.0.7
BuildRequires: erlang-p1_utils >= 1.0.5

%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
ProcessOne SIP server component in Erlang.


%prep
%setup -n %{srcname}-%{version} -q
%patch0 -p0
rm -rf ebin


%build
%{rebar_compile}


%install
%{erlang_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include
install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib

install -pm644 include/* $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include/
install -pm755 priv/lib/*.so $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib/


%check
%{rebar_eunit}


%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}



%changelog
* Sun Jan 08 2017 daviddavid <daviddavid> 1.0.8-2.mga6
+ Revision: 1080605
- rebuild to obsolete properly erlang-p1_sip

* Thu Nov 17 2016 neoclust <neoclust> 1.0.8-1.mga6
+ Revision: 1067997
- imported package erlang-esip

