# 100-puppet_ssh_config.pp
# Setting up my client config file

include stdlib

file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',
  line    => '    PasswordAuthentication no',
  match   => '^\s*PasswordAuthentication',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^\s*IdentityFile',
  replace => true,
}

file_line { 'Preferred auth method':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',
  line    => '    PreferredAuthentications publickey',
  match   => '^\s*PreferredAuthentications',
  replace => true,
}

file_line { 'Host configuration':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',
  line    => 'Host your_server_ip_or_hostname',
  match   => 'Host ',
  replace => true,
}
