%define pydict_version 0.2.5.1
%define pydict_release 13

Summary:	pyDict - An English/Chinese Dictionary written with python/gtk
Name:		pyDict
Version:	%{pydict_version}
Release:	%mkrel %{pydict_release}
Url:		http://sourceforge/projects/pydict/
License:	GPL
Group:		Text tools
Buildroot:	%_tmppath/%name-%version-%release-root

Source0:	http://sourceforge/projects/pydict/pyDict-%{pydict_version}.tar.bz2
Source1:	pyDict.desktop
Patch2:		pyDict-C2E.patch

Requires:	locales-zh pygtk

BuildRequires:  desktop-file-utils

%description
This is a English/Chinese Dictionary wirtten by Daniel Gau with python/gtk.
The word base was originally got from xdict, and was converted and modified by
Daniel Gau and bv1al.This program can be run in both console mode and X 
Window GUI mode.

%prep
%setup -q
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/X11/pyDict/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 644 yaba.xpm $RPM_BUILD_ROOT%{_libdir}/X11/pyDict/
install  -m 755 dict.py $RPM_BUILD_ROOT%{_bindir}/pydict.real
cat << EOF > pydict.sh
#!/bin/bash
# pydict only works in big5 encoding
export LC_ALL=zh_TW.Big5
exec pydict.real
EOF
install  -m 755  pydict.sh $RPM_BUILD_ROOT%{_bindir}/pydict
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Chinese
for i in a b c d e f g h i j k l m n o p q r s t u v w x y z
	do install -m 644 $i.lib $RPM_BUILD_ROOT%{_libdir}/X11/pyDict/
done
install -m 644 HELP $RPM_BUILD_ROOT%{_libdir}/X11/pyDict/

# menu XDG
install -m 644 %{SOURCE1} \
		$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Chinese/pyDict.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applnk/Chinese/

%__mkdir $RPM_BUILD_ROOT%{_datadir}/applications
%__cp  $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Chinese/pyDict.desktop $RPM_BUILD_ROOT%{_datadir}/applications/pyDict.desktop


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --add-category="Office" \
  --add-category="Dictionary" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/X11/pyDict
%doc CHANGELOG COPYING README install.sh
%{_libdir}/X11/pyDict/*
%{_datadir}/gnome/apps/Chinese/pyDict.desktop
%defattr(755,root,root,755)
%{_bindir}/pydict
%{_bindir}/pydict.real
%{_datadir}/applications/pyDict.desktop


