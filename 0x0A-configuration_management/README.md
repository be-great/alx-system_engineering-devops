#  0x0A. Configuration management

## Puppet Resource Type: File:-
- It manage the files and directories modification.
- Example:-
```bash
file { '/tmp/file':
    ensure => 'present',
    content => 'This is the test file',
    mode => '0644',
    owner => 'root',
    group => 'root',
}

exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}

```
- *ensure:*-
- present: Ensures the file or directory exists.
- absent: Ensures the file or directory does not exist.
- file: Ensures the path is a file.
- directory: Ensures the path is a directory.
- link: Ensures the path is a symlink
- *content:*- 
-  ensure the file content that file
- mode, owner, group:*-
- set the attribute of the permissions, ownership of the file
- onlyif : the command in it execute first if it's failed the exec command not executed
## Puppet’s Declarative Language: Modeling Instead of Scripting

```bash
package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  
}



```

## install :-

```bash
sudo puppet apply 1-install_a_package.pp 
```

