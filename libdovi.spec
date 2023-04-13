%undefine _debugsource_packages
%define sover 3

%define libname %mklibname dovi
%define devname %mklibname -d dovi

Name:           libdovi
Version:        3.1.2
Release:        1
Summary:        Library to read & write Dolby Vision metadata
Group:          Development/Libraries/Rust
License:        MIT
URL:            https://github.com/quietvoid/dovi_tool/tree/main/dolby_vision
Source0:        https://github.com/quietvoid/dovi_tool/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  git

%description
Library to read & write Dolby Vision metadata

%package -n %{devname}
Summary:        Development libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains C header files for
developing applications that use %{name}.

%package     -n %{libname}
Summary:        Library to read & write Dolby Vision metadata
Group:          System/Libraries

%description -n %{libname}
Library to read & write Dolby Vision metadata

%prep
%setup -a1 -q -n dovi_tool-%{name}-%{version}/dolby_vision
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
CFLAGS="%{optflags}" cargo cbuild \
    --release \
    --frozen \
    --prefix=%{_prefix} \
    --library-type=cdylib

%install
cargo cinstall \
    --release \
    --frozen \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --pkgconfigdir=%{_libdir}/pkgconfig \
    --library-type=cdylib

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.*

%files -n %{devname}
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/dovi.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/rpu_parser.h
