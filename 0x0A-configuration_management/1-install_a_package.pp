#!/usr/bin/env puppet
# create a file in /tmp

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '0.16.1',
  provider => 'pip3',
}
