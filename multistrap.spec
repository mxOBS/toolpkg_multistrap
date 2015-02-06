#
# spec file for package multistrap
#
# Copyright (c) 2015 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#
# Summary and description taken from debian package on Feb 6 2015:
#
# Copyright: 2006-2010 Neil Williams <codehelp@debian.org>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

Name: multistrap
Version: 2.1.20
Release: 1
License: GPL-3.0+
Url: https://wiki.debian.org/Multistrap
Group: Development/Tools/Building

BuildArch: noarch
Source: %{name}-%{version}.tar.xz
BuildRequires: po4a >= 0.37.1
BuildRequires: intltool

Requires: perl = %{perl_version}
Requires: perl(strict)
Requires: perl(warnings)
Requires: perl(IO::File)
Requires: perl(Config::Auto)
Requires: perl(Cwd)
Requires: perl(File::Basename)
Requires: perl(Parse::Debian::Packages)
Requires: perl(POSIX)
Requires: perl(Locale::gettext)

Summary: Multiple repository bootstrap based on apt
%description
A debootstrap replacement with multiple repository support,
using apt to handle all dependency issues and conflicts.

Multistrap includes support for native and foreign architecture
bootstrap environments. Foreign bootstraps only need minimal
configuration on the final device. Also supports cleaning up the
generated bootstrap filesystem to remove downloaded packages and
hooks to modify the files in the bootstrap filesystem after the
packages have been unpacked but before being configured.

Unlike debootstrap, multistrap relies on working versions of
dpkg and apt outside the final filesystem. If dpkg supports
MultiArch, foreign architecture libraries can be installed,
where available.

Multistrap supercedes emdebian-rootfs and replaces the previous
support for preparing root filesystems for specific machines and
variants. Multistrap includes the previous emdebian-rootfs support
for customisation of package selection and of files created
within the root filesystem.

%prep
%setup -q

%build
po4a-build
make -C po

%install
make -C po install DESTDIR=%{buildroot}
install -v -m755 -D multistrap %{buildroot}%{_sbindir}/multistrap
mkdir -p %{buildroot}%{_datadir}/multistrap
cp -v check-deps.sh device-table.pl update-rc.d cross/*.conf cross/test.c cross/setcrossarch.sh %{buildroot}%{_datadir}/multistrap
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
cp -v bash/multistrap %{buildroot}%{_sysconfdir}/bash_completion.d
mkdir -p %{buildroot}%{_docdir}/multistrap
cp -rv examples %{buildroot}%{_docdir}/multistrap
mkdir -p %{buildroot}%{_mandir}
cp -rv doc/multistrap/man/* %{buildroot}%{_mandir}
%find_lang multistrap

%files -f multistrap.lang
%defattr(-,root,root)
%{_sbindir}/multistrap
%{_datadir}/multistrap
%config %{_sysconfdir}/bash_completion.d/multistrap
%{_docdir}/multistrap
%{_mandir}/*/*/*.gz
%{_mandir}/*/*.gz

%changelog
