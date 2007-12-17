%define pydict_version 0.2.5.1
%define pydict_release 14

Summary:	pyDict - An English/Chinese Dictionary written with python/gtk
Name:		pyDict
Version:	%{pydict_version}
Release:	%mkrel %{pydict_release}
Url:		http://sourceforge.net/projects/pydict/
License:	GPL
Group:		Text tools

Source0:	http://sourceforge.net/projects/pydict/pyDict-%{pydict_version}.tar.bz2
Patch2:		pyDict-C2E.patch
Patch3:		pyDict-data-path.patch
Patch4:		pyDict-desktop.patch

Requires:	locales-zh pygtk
BuildArch:	noarch
BuildRequires:  desktop-file-utils

%description
This is a English/Chinese Dictionary wirtten by Daniel Gau with python/gtk.
The word base was originally got from xdict, and was converted and modified by
Daniel Gau and bv1al.This program can be run in both console mode and X 
Window GUI mode.

%prep
%setup -q
%patch2 -p1
%patch3 -p0
%patch4 -p0

%install
rm -rf $RPM_BUILD_ROOT

install -D -m 644 dict.xpm $RPM_BUILD_ROOT%{_iconsdir}/dict.xpm
install -D -m 644 yaba.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/yaba.xpm
install -D -m 755 dict.py $RPM_BUILD_ROOT%{_bindir}/pydict.real

cat << EOF > pydict.sh
#!/bin/bash
# pydict only works in big5 encoding
export LC_ALL=zh_TW.Big5
exec pydict.real
EOF
install  -m 755  pydict.sh $RPM_BUILD_ROOT%{_bindir}/pydict

for i in a b c d e f g h i j k l m n o p q r s t u v w x y z
	do install -m 644 $i.lib $RPM_BUILD_ROOT%{_datadir}/%{name}
done
install -m 644 HELP $RPM_BUILD_ROOT%{_datadir}/%{name}/

# menu XDG
mkdir -p %buildroot%_datadir/applications
desktop-file-install --vendor='' \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-Office-Accessories" \
	--add-category="Office" \
	--add-category="Dictionary" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%{_datadir}/%{name}
%defattr(755,root,root,755)
%{_bindir}/pydict
%{_bindir}/pydict.real
%{_iconsdir}/*
%{_datadir}/applications/pyDict.desktop
