import socket
import os
import platform
from xml.etree import ElementTree


class Platform(object):
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'

class Utils(object):
    
    STATICPATH = os.path.dirname(os.path.realpath(__file__))
    MAPPING = {}
    MAPPING[False] = 'false'
    MAPPING[True] = 'true'

    @classmethod
    def ip(cls) -> str:
        """get local ip"""
        try:
            ip = socket.gethostbyname(socket.gethostname())
        except:
            ip = '127.0.0.1'    
        return ip
    
    @classmethod
    def exec_cmd(cls, cmd: str) -> int:
        """excute command"""
        result = os.system(cmd.strip())
        return result
    
    @classmethod
    def make_dir(self, dir: str) -> str:
        if not os.path.exists(dir):
            os.mkdir(dir)
        return dir    

    @classmethod
    def make_dir_file(cls, dir : str, filename: str, content: str) -> str:
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(os.path.join(dir, filename)):
            with open(os.path.join(dir, filename), 'w', encoding="utf-8") as file:
                file.write(content)
        return os.path.join(dir, filename)        
   
    @classmethod
    def read_file_content(cls, file_path) -> str:
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            content = f.read() 
            return content            
    
    @classmethod
    def get_pc_platform(cls) -> str:
        """get current pc's platform"""
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

    @classmethod
    def read_jmxfile(cls, jmx_path_or_name: str, tag: str, name: str) -> str:
        """read text from jmx file"""
        treeDom =ElementTree.parse(jmx_path_or_name)
        rootDom = treeDom.getroot()
        tag_object = rootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['name'] == name:
                return tag_target.text
        raise Exception('no result')
    
    @classmethod
    def write_jmxfile(cls, jmx_path_or_name: str, tag: str, 
                  name: str, text: str) -> str:
        """write text to jmx file"""
        treeDom =ElementTree.parse(jmx_path_or_name)
        rootDom = treeDom.getroot()
        tag_object = rootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['name'] == name:
                tag_target.text = text
                treeDom.write(jmx_path_or_name, encoding='utf-8')
                return True
        return False    