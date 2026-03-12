#!/usr/bin/sh

if ! command -v debsecan >/dev/null 2>&1; then
	sudo apt update
	sudo apt install -y debsecan mailutils postfix
fi

cmd=$(debsecan --suite $(lsb_release --codename --short) | wc -l)

echo "Il y a $cmd CVE"

if [ $cmd -gt 1000 ]; then
	echo "Warning there is more than 1000 CVE" | mail -s "Alerte CVE" antoine.canu@univ-rouen.fr
fi
