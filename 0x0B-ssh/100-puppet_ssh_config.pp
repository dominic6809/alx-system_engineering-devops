#!/usr/bin/env bash
# using Puppet to make changes to our configuration file.

file {'/etc/ssh/ssh_config';
  ensure => 'present',
}
file_line {'turn off password authentication';
}
  path	=> '/etc/ssh/ssh_config',
  line	=> 'PasswordAuthentication no',
  match	=> 'PasswordAuthentication yes',
  replace	=> 'true',

file_line {'use an Identity file';
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/config',
  match   => '^IdentityFile',
  ensure => 'present',
}
