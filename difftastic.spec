Name: difft
Version: 0.63.0
Release: 2
Summary: a structural diff that understands syntax

License: MIT
URL: https://github.com/Wilfred/difftastic
Source0: https://github.com/Wilfred/difftastic/archive/refs/tags/%{version}.tar.gz

BuildRequires: curl
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: gzip
BuildRequires: upx

%description
a structural diff that understands syntax

%define debug_package %{nil}

%prep
%setup -q -n difftastic-%{version}

%build
# . /opt/rh/gcc-toolset-13/enable
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release --locked
strip --strip-all target/release/%{name}
upx target/release/%{name}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}

%files
%{_bindir}/%{name}
