#Execute a command

exec { 'killmenow':
  ensure  => 'killed',
  command => ['/usr/bin/pkill -f', 'killmenow']
}
