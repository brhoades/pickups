import logging
import os
import sys

import appdirs
import hangups.auth

from .server import Server

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.getLogger('hangups').setLevel(logging.WARNING)
    dirs = appdirs.AppDirs('hangups', 'hangups')
    if not os.path.exists( dirs.user_cache_dir ):
        os.mkdir( dirs.user_cache_dir )
    
    default_cookies_path = os.path.join(dirs.user_cache_dir, 'cookies.json')
    if len(sys.argv) > 3: 
        print( sys.argv[3] )
        default_cookies_path = sys.argv[3]

    cookies = hangups.auth.get_auth_stdin(default_cookies_path)
    if len(sys.argv) > 2:
        Server(cookies=cookies).run( sys.argv[1], sys.argv[2] )
    else:
        Server(cookies=cookies).run('localhost', 6667)
