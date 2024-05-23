# Script that installs and configures Nginx
exec {'update':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y update',
}

exec {'install':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get -y install nginx',
}

exec {'echo_html':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html',
}

exec {'sed_config':
  command  =>  '/usr/bin/sudo /bin/sed -i "66i rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}

exec {'start':
  command  => 'sudo service nginx start',
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
}
