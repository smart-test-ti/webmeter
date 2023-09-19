import os
import shutil
from loguru import logger
from webmeter.core.utils import Common, JMX
from fastapi import UploadFile

class Base(object):

    @classmethod
    def info(cls, plan_jmx_path: str) -> dict:
        """read plan base info"""
        plan_info_dict = dict()
        plan_info_dict['name'] = JMX.read_testname(
            jmx_path_or_name=plan_jmx_path, 
            tag='TestPlan', 
            attr='TestPlan',
            default='TestPlan')
        plan_info_dict['comments'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='TestPlan.comments', 
            default='')
        plan_info_dict['functional_mode'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='boolProp', 
            name='TestPlan.functional_mode',
            default='false'))
        plan_info_dict['tearDown_on_shutdown'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='TestPlan.tearDown_on_shutdown',
            default='true'))
        plan_info_dict['serialize_threadgroups'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='boolProp', 
            name='TestPlan.serialize_threadgroups',
            default='false'))
        return plan_info_dict
    
    @classmethod
    def save(cls, jmx_path: str, content: dict) -> None:
        logger.info(content)
        JMX.write_testname(jmx_path,'TestPlan','TestPlan', content.get('new_plan_name'))
        JMX.write_text(jmx_path, 'stringProp', 'TestPlan.comments', content.get('plan_comment'))
        JMX.write_text(jmx_path, 'boolProp', 'TestPlan.functional_mode', Common.MAPPING.get(content.get('functional_mode')))
        JMX.write_text(jmx_path, 'boolProp', 'TestPlan.tearDown_on_shutdown', Common.MAPPING.get(content.get('tearDown_on_shutdown')))
        JMX.write_text(jmx_path, 'boolProp', 'TestPlan.serialize_threadgroups', Common.MAPPING.get(content.get('serialize_threadgroups')))
    
class Thread_Group(object):

    @classmethod
    def info(cls, plan_jmx_path: str) -> dict:
        """read thread group info"""
        thread_group_info_dict = dict()
        thread_group_info_dict['thread_group_name'] = JMX.read_testname(
            jmx_path_or_name=plan_jmx_path, 
            tag='ThreadGroup', 
            attr='ThreadGroup',
            default='ThreadGroup')
        thread_group_info_dict['thread_group_comment'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='TestPlan.comments',
            default=None)
        thread_group_info_dict['on_sample_error'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.on_sample_error',
            default='continue')
        thread_group_info_dict['num_threads'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.num_threads',
            default='1')
        thread_group_info_dict['ramp_time'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.ramp_time',
            default='1')
        thread_group_info_dict['loops'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='stringProp', 
            name='LoopController.loops',
            default='1')
        thread_group_info_dict['same_user_on_next_iteration'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.same_user_on_next_iteration',
            default='true'))
        thread_group_info_dict['delayedStart'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.delayedStart',
            default='false'))
        thread_group_info_dict['scheduler'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.scheduler',
            default='false'))
        thread_group_info_dict['duration'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.duration',
            default='')
        thread_group_info_dict['delay'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.delay',
            default='')
        logger.info(thread_group_info_dict)
        return thread_group_info_dict
    
    @classmethod
    def save(cls, jmx_path: str, content: dict):
        logger.info(content)
        JMX.write_testname(jmx_path,'ThreadGroup','ThreadGroup', content.get('thread_group_name'))
        JMX.write_text(jmx_path, 'stringProp', 'ThreadGroup.on_sample_error', content.get('on_sample_error'))
        JMX.write_text(jmx_path, 'stringProp', 'ThreadGroup.num_threads', content.get('num_threads'))
        JMX.write_text(jmx_path, 'stringProp', 'ThreadGroup.ramp_time', content.get('ramp_time'))
        JMX.write_text(jmx_path, 'stringProp', 'LoopController.loops', content.get('loops'))
        JMX.write_text(jmx_path, 'boolProp', 'ThreadGroup.same_user_on_next_iteration', 
                       Common.MAPPING.get(content.get('same_user_on_next_iteration')))
        JMX.write_text(jmx_path, 'boolProp', 'ThreadGroup.delayedStart', Common.MAPPING.get(content.get('delayedStart')))
        JMX.write_text(jmx_path, 'boolProp', 'ThreadGroup.scheduler', Common.MAPPING.get(content.get('scheduler')))
        JMX.write_text(jmx_path, 'stringProp', 'ThreadGroup.duration', content.get('loodurationps'))
        JMX.write_text(jmx_path, 'stringProp', 'ThreadGroup.delay', content.get('delay'))

class Samplers(object):
    
    @classmethod
    def info(cls, plan_jmx_path: str) -> list:
        """get samplers info"""
        samplers_info_dict = dict()
        samplers_info_dict['http_request_name'] = JMX.read_testname(
            jmx_path_or_name=plan_jmx_path, 
            tag='HTTPSamplerProxy', 
            attr='HTTPSamplerProxy',
            default='Http Request')
        samplers_info_dict['protocol'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.protocol',
            default='')
        samplers_info_dict['domain'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.domain',
            default='')
        samplers_info_dict['port'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.port',
            default='')
        samplers_info_dict['method'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.method',
            default='')
        samplers_info_dict['path'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.path',
            default='')
        samplers_info_dict['contentEncoding'] = JMX.read_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='HTTPSampler.contentEncoding',
            default='')
        samplers_info_dict['follow_redirects'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.follow_redirects',
            default='true'))
        samplers_info_dict['auto_redirects'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.auto_redirects',
            default='false'))
        samplers_info_dict['use_keepalive'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.use_keepalive',
            default='true'))
        samplers_info_dict['DO_MULTIPART_POST'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.DO_MULTIPART_POST',
            default='false'))
        samplers_info_dict['BROWSER_COMPATIBLE_MULTIPART'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.BROWSER_COMPATIBLE_MULTIPART',
            default='false'))
        samplers_info_dict['parameters'] = JMX.read_proxy(plan_jmx_path)
        samplers_info_dict['postBodyRaw'] = Common.MAPPING.get(JMX.read_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='HTTPSampler.postBodyRaw',
            default='false'))
        if samplers_info_dict['postBodyRaw']:
            samplers_info_dict['body_data'] = JMX.read_text(
                jmx_path_or_name=plan_jmx_path, 
                tag='stringProp', 
                name='Argument.value',
                default='{}')
        logger.info(samplers_info_dict)
        return samplers_info_dict
    
    @classmethod
    def save(cls, jmx_path: str, content: dict):
        logger.info(content)
        JMX.write_testname(jmx_path,'HTTPSamplerProxy','HTTPSamplerProxy', content.get('http_request_name'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.protocol', content.get('protocol'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.domain', content.get('domain'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.port', content.get('port'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.method', content.get('method'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.path', content.get('path'))
        JMX.write_text(jmx_path, 'stringProp', 'HTTPSampler.contentEncoding', content.get('contentEncoding'))
        JMX.write_text(jmx_path, 'boolProp', 'HTTPSampler.follow_redirects', 
                       Common.MAPPING.get(content.get('follow_redirects')))
        JMX.write_text(jmx_path, 'boolProp', 'HTTPSampler.auto_redirects', 
                       Common.MAPPING.get(content.get('auto_redirects')))
        JMX.write_text(jmx_path, 'boolProp', 'HTTPSampler.use_keepalive', 
                       Common.MAPPING.get(content.get('use_keepalive')))
        JMX.write_text(jmx_path, 'boolProp', 'HTTPSampler.DO_MULTIPART_POST', 
                       Common.MAPPING.get(content.get('DO_MULTIPART_POST')))
        JMX.write_text(jmx_path, 'boolProp', 'HTTPSampler.BROWSER_COMPATIBLE_MULTIPART', 
                       Common.MAPPING.get(content.get('BROWSER_COMPATIBLE_MULTIPART')))
        JMX.write_text(jmx_path, 'stringProp', 'Argument.value', content.get('body_data'))


class TestPlan(Base, Thread_Group, Samplers):

    def __init__(self):
        self.file_dir = os.path.join(Common.STATICPATH, 'file')
        self.template_jmx_path = os.path.join(self.file_dir, 'template.jmx')
        self.root_dir = Common.make_dir(os.path.join(os.getcwd(), 'webmeter'))


    def create(self, plan_name: str) -> str:
        """create new plan"""
        content = Common.read_file_content(self.template_jmx_path)
        plan_dir = Common.make_dir(os.path.join(self.root_dir, plan_name))
        plan_path = Common.make_dir_file(dir=plan_dir, filename='plan.jmx', content=content)
        JMX.write_testname(jmx_path_or_name=os.path.join(self.root_dir, plan_name, 'plan.jmx'),
                                     tag='TestPlan', attr='TestPlan', testname=plan_name)
        logger.info('create plan success: {}'.format(plan_path))
        return plan_path
    
    def import_jmx(self, file: UploadFile, plan_name: str) -> str:
        """import new plan"""
        plan_dir = Common.make_dir(os.path.join(self.root_dir, plan_name))
        jmx_name = file.filename
        jmx_path = os.path.join(self.root_dir, plan_name, jmx_name)
        with open(jmx_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        content = Common.read_file_content(jmx_path)
        os.remove(jmx_path)
        plan_path = Common.make_dir_file(dir=plan_dir, filename='plan.jmx', content=content)
        JMX.write_testname(jmx_path_or_name=os.path.join(self.root_dir, plan_name, 'plan.jmx'),
                                     tag='TestPlan', attr='TestPlan', testname=plan_name)
        logger.info('import plan success: {}'.format(plan_path))
        return plan_path

    def isexist(self, plan_name: str) -> bool:
        if os.path.exists(os.path.join(self.root_dir, plan_name)):
            return True
        return False
    
    def info(self, plan: str) -> dict:
        """get one plan info"""
        result = dict()
        plan_jmx_path = os.path.join(self.root_dir, plan, 'plan.jmx')
        plan_base_info = Base.info(plan_jmx_path)
        thread_group_info = Thread_Group.info(plan_jmx_path)
        samplers_info = Samplers.info(plan_jmx_path)
        result.update(plan_base_info)
        result.update(thread_group_info)
        result.update(samplers_info)
        return result
    
    def edit(self, content: dict) -> None:
        """edit plan content"""
        jmx_path = os.path.join(self.root_dir, content['old_plan_name'], 'plan.jmx')
        # edit plan info
        Base.save(jmx_path, content)
        Thread_Group.save(jmx_path, content)
        Samplers.save(jmx_path, content)
        old_plan_dir = os.path.join(self.root_dir, content['old_plan_name'])
        new_plan_dir = os.path.join(self.root_dir, content['new_plan_name'])
        os.rename(old_plan_dir, new_plan_dir)

    def remove(self, plan: str) -> None:
        """remove one plan"""
        shutil.rmtree(os.path.join(self.root_dir, plan), True)
        logger.warning('remove {} success'.format(plan))
    
    def remove_all(self) -> None:
        """remove all plan"""
        dirs = os.listdir(self.root_dir)
        for plan in dirs:
            shutil.rmtree(os.path.join(self.root_dir, plan), True)
            logger.warning('remove {} success'.format(plan))

    def get_all_plan(self) -> list:
        """get all plan"""
        dirs = os.listdir(self.root_dir)
        dir_list = reversed(sorted(dirs, key=lambda x: os.path.getmtime(os.path.join(self.root_dir, x))))
        plan_sorted_list = [plan for plan in dir_list if plan.__contains__('.') is False]
        plan_list = list()
        for plan in plan_sorted_list:
            plan_dict = dict()
            plan_dict['name'] = plan
            plan_dict['checked'] =True if plan_sorted_list.index(plan) == 0 else False
            plan_list.append(plan_dict)
        return plan_list
    
    def checked_one_plan(self, plan_name) -> list:
        """checked one plan"""
        dirs = os.listdir(self.root_dir)
        dir_list = reversed(sorted(dirs, key=lambda x: os.path.getmtime(os.path.join(self.root_dir, x))))
        plan_sorted_list = [plan for plan in dir_list if plan.__contains__('.') is False]
        plan_list = list()
        for plan in plan_sorted_list:
            plan_dict = dict()
            plan_dict['name'] = plan
            plan_dict['checked'] =True if plan == plan_name else False
            plan_list.append(plan_dict)
        return plan_list