import socket
import os
import enum
import platform
from loguru import logger
from xml.etree import ElementTree


class Platform(enum.Enum):
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'

class Utils(object):
    
    STATICPATH = os.path.dirname(os.path.realpath(__file__))
    MAPPING = dict()
    MAPPING[False] = 'false'
    MAPPING[True] = 'true'
    MAPPING['false'] = False
    MAPPING['true'] = True

    @classmethod
    def ip(cls) -> str:
        """get local ip"""
        try:
            ip = socket.gethostbyname(socket.gethostname())
        except:
            logger.info('hostname:{}'.format(socket.gethostname()))
            logger.warning('config [127.0.0.1 hostname] in /etc/hosts file')
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
    def pc_platform(cls) -> str:
        """get pc platform"""
        sys_platform = platform.platform().lower()
        match sys_platform:
            case sys_platform.__contains__(Platform.WINDOWS.value):
                return Platform.WINDOWS.value
            case sys_platform.__contains__(Platform.MACOS.value):
                return Platform.MACOS.value
            case sys_platform.__contains__(Platform.LINUX.value):
                return Platform.LINUX.value
            case _:
                raise Exception('platform is invalid')

    @classmethod
    def read_jmxfile_text(cls, jmx_path_or_name: str, tag: str, name: str) -> str:
        """read text from jmx file"""
        treeDom =ElementTree.parse(jmx_path_or_name)
        rootDom = treeDom.getroot()
        tag_object = rootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['name'] == name:
                return tag_target.text
        raise Exception('no result')
    
    @classmethod
    def read_jmxfile_testname(cls, jmx_path_or_name: str, tag: str, attr: str) -> str:
        """read attr from jmx file"""
        treeDom =ElementTree.parse(jmx_path_or_name)
        rootDom = treeDom.getroot()
        tag_object = rootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['testclass'] == attr:
                return tag_target.attrib['testname']
        raise Exception('no result')
    
    @classmethod
    def write_jmxfile_testname(cls, jmx_path_or_name: str, tag: str, 
                  attr: str, testname: str) -> str:
        """update testname to jmx file"""
        treeDom =ElementTree.parse(jmx_path_or_name)
        rootDom = treeDom.getroot()
        tag_object = rootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['testclass'] == attr:
                tag_target.attrib['testname'] = testname
                treeDom.write(jmx_path_or_name, encoding='utf-8')
                return True
        return False
    
    @classmethod
    def write_jmxfile_text(cls, jmx_path_or_name: str, tag: str, 
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