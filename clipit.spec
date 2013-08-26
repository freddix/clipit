Summary:	Lightweight GTK+ clipboard manager
Name:		clipit
Version:	1.4.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/downloads/shantzu/ClipIt/%{name}-%{version}.tar.gz
# Source0-md5:	118175f26869adcf04909fdbb5021eff
URL:		http://clipit.rspwn.com/
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Suggests:	xdotool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lightweight GTK+ clipboard manager (fork of Parcellite).

%prep
%setup -q

%{__sed} -i "s|GNOME;Application;||" data/clipit.desktop.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES

%find_lang %{name}

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/clipit-startup.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/clipit.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clipit
%{_sysconfdir}/xdg/autostart/clipit-startup.desktop
%{_desktopdir}/clipit.desktop
%{_iconsdir}/hicolor/scalable/apps/clipit-trayicon.svg
%{_mandir}/man1/clipit.1*

