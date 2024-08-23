# Automating the Nginx configurations with puppet

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location = /redirect_me {
        return 301 https://www.youtube.com/@dominicmusyoki804;
    }

    location = / {
        try_files \$uri \$uri/ =404;
    }
}
  ",
  notify  => Service[ 'nginx' ],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
