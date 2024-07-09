# Add a custom HTTP header with Puppet
exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx'],
}

exec { 'install nginx':
  provider => shell,
  command  => 'sudo apt-get install -y nginx',
  before   => Exec['nginx config'],
}

exec { 'nginx config':
  provider     => shell,
  environment  => ["host=${hostname}"],
  command      => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$host\";/" /etc/nginx/nginx.conf',
  before       => Exec['restart nginx'],
}

exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
