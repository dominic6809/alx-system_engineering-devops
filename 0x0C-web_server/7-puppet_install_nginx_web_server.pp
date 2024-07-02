# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Create a custom index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Backup the default site configuration file
file { '/etc/nginx/sites-available/default.bak':
  ensure  => file,
  content => file('/etc/nginx/sites-available/default'),
  require => Package['nginx'],
}

# Configure Nginx to set up the redirect and serve the custom page
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the Nginx configuration template
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
',
  require => Package['nginx'],
}
