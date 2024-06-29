# This Puppet manifest ensures that the file /tmp/school exists
# with the desired permissions, ownership, and content.

file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
