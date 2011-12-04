Name: hunspell-fr
Summary: French hunspell dictionaries
Version: 3.4
Release: 1.1%{?dist}
Source: http://www.dicollecte.org/download/fr/hunspell_fr_3-4.zip
Group: Applications/Text
URL: http://www.dicollecte.org/home.php?prj=fr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2 or LGPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
French (France, Belgium, etc.) hunspell dictionaries.

%prep
%setup -q -c -n hunspell-fr

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p fr.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/fr_FR.dic
cp -p fr.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/fr_FR.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
	ln -s fr_FR.aff $lang.aff
	ln -s fr_FR.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_fr.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.4-1.1
- Rebuilt for RHEL 6

* Fri Sep 11 2009 Caolan McNamara <caolanm@redhat.com> - 3.4-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Caolan McNamara <caolanm@redhat.com> - 3.2-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Caolan McNamara <caolanm@redhat.com> - 2.3.2-1
- latest version

* Tue Apr 22 2008 Caolan McNamara <caolanm@redhat.com> - 2.3.1-1
- latest version

* Mon Mar 10 2008 Caolan McNamara <caolanm@redhat.com> - 2.2.0-1
- latest version

* Thu Feb 07 2008 Caolan McNamara <caolanm@redhat.com> - 2.1.0-1
- latest version

* Fri Dec 21 2007 Caolan McNamara <caolanm@redhat.com> - 2.0.5-1
- project moved to http://dico.savant.free.fr and a new release

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060915-2
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20060915-1
- initial version
