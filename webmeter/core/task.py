from loguru import logger
import json, os
from core.utils import Common
from typing import Optional

class TaskBase(object):

    ROOT_DIR = Common.make_dir(os.path.join(os.getcwd(), 'webmeter'))

    @classmethod
    def read_statistics_file(cls, plan: str, task: str) -> dict:
        """read statistics.json content"""
        statistics_file_path = os.path.join(cls.ROOT_DIR, plan, 'report', task,'statistics.json')
        content = Common.read_file_content(statistics_file_path)
        if content:
            return json.loads(content)
        else:
            raise Exception('No content found in the statistics.json')
        
    @classmethod
    def read_result_file(cls, plan: str, task: str):
        """read result.jtl content"""
        result_file_path = os.path.join(cls.ROOT_DIR, plan, 'report', task,'result.jtl')
        content = Common.read_file_content(result_file_path)
        if content:
            return content
        else:
            raise Exception('No content found in the result.jtl')

    @classmethod
    def read_log(cls, plan: str, task: str) -> Optional[str]:
        """read result.log content"""
        log_file_path = os.path.join(cls.ROOT_DIR, plan, 'log', task,'result.log')
        content = Common.read_file_content(log_file_path)
        if content:
            return content
        else:
            raise Exception('No content found in the result.log')
