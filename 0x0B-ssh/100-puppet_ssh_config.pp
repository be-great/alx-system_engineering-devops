# using Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# Your machine has an SSH configuration
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
  mode    => "0744",
  owner   => "test",
  group   => "test",
}
