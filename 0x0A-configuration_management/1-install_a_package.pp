# Using Puppet, create a file in /tmp
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}