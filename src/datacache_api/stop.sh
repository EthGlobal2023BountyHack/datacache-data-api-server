kill -9 $(ps aux | grep datacache | awk '{print $2}')
