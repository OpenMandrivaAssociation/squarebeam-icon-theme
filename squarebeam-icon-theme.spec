%global theme	Square-Beam-KDE

Name:		squarebeam-icon-theme
Version:	1.0
Release:	1
Summary:	%{theme} icon theme
Group:		Graphical desktop/Other

License:	GPL
URL:		https://kde-look.org/content/show.php/?content=165154

Source0:	http://code.emka.web.id/demo/square-beam-kde/%{theme}_%{version}.tar.gz

BuildArch:	noarch

%description
%{theme} Icons set for Linux distribution.
First release but more than 30.000 icons included in the icons set. 
Icon designed by EepSetiawan


%prep
%setup -q -n %{theme}



%build
chmod -R 0755 %{_builddir}/%{theme}/*

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/%{theme}
cp -axv %{_builddir}/%{theme}/* %{buildroot}%{_datadir}/icons/%{theme}


%files
%{_datadir}/icons/%{theme}
