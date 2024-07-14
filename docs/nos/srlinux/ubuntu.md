sudo ln -s /etc/apparmor.d/usr.sbin.rsyslogd /etc/apparmor.d/disable/

sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.rsyslogd