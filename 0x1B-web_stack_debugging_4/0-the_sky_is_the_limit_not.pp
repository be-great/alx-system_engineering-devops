# update the max limt on the nginx server

exec {'update_max_limit':
  command => 'sed -i "s/\b15\b/10000/" /etc/default/nginx && service nginx restart',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif  => 'grep -q "\b15\b" /etc/default/nginx',
}
