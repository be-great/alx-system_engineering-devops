# change os config to login with holbertion user
exec {'security_confg':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}
