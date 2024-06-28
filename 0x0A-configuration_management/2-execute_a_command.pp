# a manifest that kills a process named killmenow.

exec { 'kill_killmenow_process':
    command => 'pkill -f killmenow',
    path    => ['/bin', '/usr/bin'],
    onlyif => 'pgrep -f killmenow',
}
