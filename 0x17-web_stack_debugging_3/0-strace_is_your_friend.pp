# fix wrong extension of a wordpress file setting  from "phpp" to "php"
exec { 'fixing-wordpress-file':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-setting.phpp',
  path    => '/usr/local/bin:/bin:/usr/bin',
}
