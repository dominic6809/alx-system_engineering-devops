#!/usr/bin/env bash
# using Puppet to make changes to our configuration file.
exec { 'Append Line IdentityFile':
  command => '/bin/echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
