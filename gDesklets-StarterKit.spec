%define		pname	StarterKit
Summary:	This package contains some basic sensors and nice displays
Summary(pl):	Ten pakiet zawiera kilka podstawowych czujników i ³adnych wy¶wietlaczy
Name:		gDesklets-%{pname}
Version:	1
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{pname}.tar.bz2
# Source0-md5:	aba8937993b2d791c3b0cd7f60c75d22
URL:		http://www.pycage.de/software_gdesklets.html
BuildRequires:	python >= 2.3
Requires:	gDesklets
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some basic sensors and nice displays.

%description -l pl
Ten pakiet zawiera kilka podstawowych czujników i ³adnych
wy¶wietlaczy.

%prep
%setup -q -n %{pname}
tail -c 10240 Install_ACPI_Sensor.bin 2>&1 | tar -xz 2>&1
tail -c 10240 Install_Clock_Sensor.bin 2>&1 | tar -xz 2>&1
#tail -c 10240 Install_External_Sensor.bin 2>&1 | tar -xz 2>&1
#tail -c 20480 Install_Weather_Sensor.bin 2>&1 | tar -xz 2>&1

rm -rf Weather/locale/de/{CVS,LC_MESSAGES/CVS}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/{Sensors,Displays/%{pname}}

cp -R ACPI Clock $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors

rm -f $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*
