import socket
import os
import sys
import platform

class Platform(object):
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'

class Utils(object):

    @classmethod
    def local_ip(cls):
        ip = socket.gethostbyname(socket.gethostname())
        return ip
    
    @classmethod
    def exe_cmd(cls, cmd):
        result = os.system(cmd)
        return result
    
    @classmethod
    def cur_platform(cls):
        sys_platform = platform.platform().lower()
        match sys_platform:
            case sys_platform.__contains__(Platform.WINDOWS):
                return Platform.WINDOWS
            case sys_platform.__contains__(Platform.MACOS):
                return Platform.MACOS
            case sys_platform.__contains__(Platform.LINUX):
                return Platform.LINUX
            case _:
                raise Exception('platform is invalid')

