# https://stackoverflow.com/questions/4731364/internal-error-500-apache-but-nothing-in-the-logs
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
