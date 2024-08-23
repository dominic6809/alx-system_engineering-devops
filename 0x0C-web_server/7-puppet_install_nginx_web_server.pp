# Automating the web configurations with puppet

# install Nginx with puppet
package { 'nginx';
  ensure => installed,
}

file_line { 'install';
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/@dominicmusyoki804 permanent;',
}

file { '/var/www/html/index.html';
  content  => 'Hello World!',
}

service { 'nginx';
  ensure  => running,
  require =>Package['nginx'],
}
