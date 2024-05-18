# puppet code to install and configure nginx

#check if nginx is installed
package {'nginx':
ensure => 'present',
}

#install and update
exec {'install_update':
command  => 'sudo apt-get update; sudo apt-get -y install nginx',
provider => shell,
}

#homepage
exec {'homepage':
command  => 'echo "Hello World!" > /var/www/html/index.html',
provider => shell,
}

#redirect me page
exec {'redirect_me':
command  => 'echo "https://www.youtube.com/watch?v=QH2-TGUlwu4" > /var/www/html/redirect_me',
provider => shell,
}

#configure nginx for redirect me
exec {'nginx_config':
provider => shell,
command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.youtube.com permanent;" /etc/nginx/sites-available/default',
}

#start server
exec {'start_server':
command  => 'sudo service nginx start',
provider => shell,
}
