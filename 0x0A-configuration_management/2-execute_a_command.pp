#Execute a command

exec { 'killmenow':
  ensure  => 'killed',
  command => ['pkill', 'killmenow']
}
