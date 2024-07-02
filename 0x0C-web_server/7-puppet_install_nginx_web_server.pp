#  Install Nginx web server (w/ Puppet) 

exec { 'apt update':
  command => '/usr/bin/apt-get update -y'

}
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt update'],
}

# Create a custom index.html file with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => "sed -i '24i\\rewrite ^/redirect_me https://example.com permanent;' /etc/nginx/sites-available/default",
  provider => 'shell',
}

service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],

}