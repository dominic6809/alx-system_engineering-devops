#!/usr/bin/env bash
# using puppet to make changes to config file

file { '/etc/ssh/ssh_config':
	ensure => present,

content =>"

	# client config
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
