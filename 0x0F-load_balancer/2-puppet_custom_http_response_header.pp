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
  provider => shell,
  command  => 'printf "%s\n\tadd_header X-Served-By \\"$HOST\\";" "$(grep -v "add_header X-Served-By" /etc/nginx/nginx.conf)" > /tmp/nginx.conf && sudo mv /tmp/nginx.conf /etc/nginx/nginx.conf',
  before   => Exec['restart nginx'],
}

exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
