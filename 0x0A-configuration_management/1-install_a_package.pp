#install flask using python
exec {'flask_install':
  command => 'pip3 install Flask==2.1.0',
  path    =>'usr/local/bin',
unless    => 'pip3 show Flask | grep Version | grep -q 2.1.0',
}
