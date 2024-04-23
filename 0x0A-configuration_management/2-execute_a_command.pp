#using exec
exec{'pikill meow':
command => 'pkill -f killmenow',
path    => '/usr/bin:/bin',
onlyif  => 'pgrep -f killmenow'
}
