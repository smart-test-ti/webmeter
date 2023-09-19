import socket
import os
from enum import Enum, unique
import platform
from loguru import logger
from xml.etree import ElementTree
from typing import Optional
from contextlib import contextmanager


@unique
class Platform(Enum):
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'
    
class Common(object):
    
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
    
    @contextmanager
    @classmethod
    def open_file(cls, path, mode):
        try:
            file = open(path, mode)
            yield file
        except Exception as e:
            raise e    
        finally:
            file.close()

    @classmethod
    def exec_cmd(cls, cmd: str) -> int:
        """execute command"""
        logger.info('start command : {}'.format(cmd))
        result = os.system(cmd.strip())
        return result
    
    @classmethod
    def make_dir(cls, dir: str) -> str:
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
    def read_file_lines(cls, file_path) -> list:
        with open(file=file_path, mode='r', encoding='utf-8') as f:
            content = f.readlines() 
            return content        
    
    @classmethod
    def pc_platform(cls) -> Optional[str]:
        """get pc platform"""
        sys_platform = platform.platform().lower()
        if sys_platform.__contains__(Platform.WINDOWS.value):
            return Platform.WINDOWS.value
        elif sys_platform.__contains__(Platform.MACOS.value):
            return Platform.MACOS.value
        elif sys_platform.__contains__(Platform.LINUX.value):
            return Platform.LINUX.value
        else:
            logger.error('platform is undefined')
            return None
        

class JMX(object):

    @classmethod
    def read_text(cls, jmx_path_or_name: str, tag: str, 
                  name: str, default: any) -> any:
        """read text from jmx file"""
        jmxElementTreeDom =ElementTree.parse(jmx_path_or_name)
        jmxElementRootDom = jmxElementTreeDom.getroot()
        tag_object = jmxElementRootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['name'] == name:
                return tag_target.text
        logger.warning('no found {}'.format(name))
        return default
    
    @classmethod
    def read_text_list(cls, jmx_path_or_name: str, tag: str, 
                  name: str, key: str) -> list:
        """read text list from jmx file"""
        element_list = list()
        element_dict = dict()
        jmxElementTreeDom =ElementTree.parse(jmx_path_or_name)
        jmxElementRootDom = jmxElementTreeDom.getroot()
        tag_object = jmxElementRootDom.iter(tag)
        for tag_target in tag_object:
            tag_dict = dict()
            if tag_target.attrib['name'] == name:
                element_dict[key] = tag_target.text
                tag_dict.update(element_dict)
                element_list.append(tag_dict)
        return element_list
    
    @classmethod
    def read_proxy(cls, jmx_path_or_name: str) -> list:
        """read text from jmx file"""
        name_list = cls.read_text_list(jmx_path_or_name=jmx_path_or_name,
                                       tag='stringProp',
                                       name='Argument.name',
                                       key='name')        
        value_list = cls.read_text_list(jmx_path_or_name=jmx_path_or_name,
                                        tag='stringProp',
                                        name='Argument.value',
                                        key='value')
        metadata_list = cls.read_text_list(jmx_path_or_name=jmx_path_or_name,
                                        tag='stringProp',
                                        name='Argument.metadata',
                                        key='metadata')
        use_equals_list = cls.read_text_list(jmx_path_or_name=jmx_path_or_name,
                                        tag='boolProp',
                                        name='HTTPArgument.use_equals',
                                        key='use_equals')
        always_encode_list = cls.read_text_list(jmx_path_or_name=jmx_path_or_name,
                                        tag='boolProp',
                                        name='HTTPArgument.always_encode',
                                        key='always_encode')
        proxy_list = list()
        for i in range(len(name_list)):
            name_list[i].update(value_list[i])
            name_list[i].update(metadata_list[i])
            name_list[i].update(use_equals_list[i])
            name_list[i].update(always_encode_list[i])
            proxy_list.append(name_list[i])
        return proxy_list
    
    @classmethod
    def read_testname(cls, jmx_path_or_name: str, tag: str,
                      attr: str, default: any) -> any:
        """read attr from jmx file"""
        jmxElementTreeDom =ElementTree.parse(jmx_path_or_name)
        jmxElementRootDom = jmxElementTreeDom.getroot()
        tag_object = jmxElementRootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['testclass'] == attr:
                return tag_target.attrib['testname']
        logger.warning('no found {}'.format(attr))
        return default
    
    @classmethod
    def write_testname(cls, jmx_path_or_name: str, tag: str,
                       attr: str, testname: str) -> str:
        """update testname to jmx file"""
        jmxElementTreeDom =ElementTree.parse(jmx_path_or_name)
        jmxElementRootDom = jmxElementTreeDom.getroot()
        tag_object = jmxElementRootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['testclass'] == attr:
                tag_target.attrib['testname'] = testname
                jmxElementTreeDom.write(jmx_path_or_name, encoding='utf-8')
                return True
        return False
    
    @classmethod
    def write_text(cls, jmx_path_or_name: str, tag: str,
                   name: str, text: str) -> str:
        """write text to jmx file"""
        jmxElementTreeDom =ElementTree.parse(jmx_path_or_name)
        jmxElementRootDom = jmxElementTreeDom.getroot()
        tag_object = jmxElementRootDom.iter(tag)
        for tag_target in tag_object:
            if tag_target.attrib['name'] == name:
                tag_target.text = text
                jmxElementTreeDom.write(jmx_path_or_name, encoding='utf-8')
                return True
        return False