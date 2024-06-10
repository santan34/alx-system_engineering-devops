# puppet file to automate a 500 error fix
exec { 'phpp-fix':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
