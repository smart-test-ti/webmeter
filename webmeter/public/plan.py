import os
import shutil
from loguru import logger
from public.utils import Utils

class TestPlan(object):

    def __init__(self):
        self.file_dir = os.path.join(Utils.STATICPATH, 'file')
        self.template_jmx_path = os.path.join(self.file_dir, 'template.jmx')
        self.root_dir = Utils.make_dir(os.path.join(os.getcwd(), 'webmeter'))


    def create(self, plan_name: str) -> str:
        """create new plan"""
        content = Utils.read_file_content(self.template_jmx_path)
        plan_dir = Utils.make_dir(os.path.join(self.root_dir, plan_name))
        plan_path = Utils.make_dir_file(dir=plan_dir, filename='plan.jmx', content=content)
        Utils.write_jmxfile_testname(jmx_path_or_name=os.path.join(self.root_dir, plan_name, 'plan.jmx'),
                                     tag='TestPlan', attr='TestPlan', testname=plan_name)
        logger.info('create plan success: {}'.format(plan_path))
        return plan_path
    
    def isexist(self, plan_name: str) -> bool:
        if os.path.exists(os.path.join(self.root_dir, plan_name)):
            return True
        return False
    
    def edit(self, content: dict) -> None:
        """edit plan content"""
        old_dir = os.path.join(self.root_dir, content['old_name'])
        new_dir = os.path.join(self.root_dir, content['new_name'])
        os.rename(old_dir, new_dir)
        # edit plan info
        element_dict = dict()
        element_dict['TestPlan.comments'] = content['comments']
        element_dict['TestPlan.functional_mode'] = content['functional_mode']
        element_dict['TestPlan.tearDown_on_shutdown'] = content['tearDown_on_shutdown']
        element_dict['TestPlan.serialize_threadgroups'] = content['serialize_threadgroups']
        for key in element_dict.keys():
            Utils.write_jmxfile_text(new_dir, 'stringProp', key, element_dict[key])

    def remove(self, plan: str) -> None:
        """remove one plan"""
        shutil.rmtree(os.path.join(self.root_dir, plan), True)
        logger.info('remove {} success'.format(plan))
    
    def remove_all(self) -> None:
        """remove all plan"""
        dirs = os.listdir(self.root_dir)
        for plan in dirs:
            shutil.rmtree(os.path.join(self.root_dir, plan), True)
            logger.info('remove {} success'.format(plan))

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
    
    def plan_base_info(self, plan_jmx_path: str) -> dict:
        """read plan base info"""
        plan_info_dict = dict()
        plan_info_dict['name'] = Utils.read_jmxfile_testname(
            jmx_path_or_name=plan_jmx_path, 
            tag='TestPlan', 
            attr='TestPlan',
            default='TestPlan')
        plan_info_dict['comments'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='TestPlan.comments', 
            default='')
        plan_info_dict['functional_mode'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='boolProp', 
            name='TestPlan.functional_mode',
            default='false'))
        plan_info_dict['tearDown_on_shutdown'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='TestPlan.tearDown_on_shutdown',
            default='true'))
        plan_info_dict['serialize_threadgroups'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='boolProp', 
            name='TestPlan.serialize_threadgroups',
            default='false'))
        return plan_info_dict
    
    def thread_group_info(self, plan_jmx_path: str) -> dict:
        """read thread group info"""
        thread_group_info_dict = dict()
        thread_group_info_dict['thread_group_name'] = Utils.read_jmxfile_testname(
            jmx_path_or_name=plan_jmx_path, 
            tag='ThreadGroup', 
            attr='ThreadGroup',
            default='ThreadGroup')
        thread_group_info_dict['thread_group_comment'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='TestPlan.comments',
            default=None)
        thread_group_info_dict['on_sample_error'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.on_sample_error',
            default='continue')
        thread_group_info_dict['num_threads'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.num_threads',
            default='1')
        thread_group_info_dict['ramp_time'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.ramp_time',
            default='1')
        thread_group_info_dict['loops'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path,
            tag='stringProp', 
            name='LoopController.loops',
            default='1')
        thread_group_info_dict['same_user_on_next_iteration'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.same_user_on_next_iteration',
            default='true'))
        thread_group_info_dict['delayedStart'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.delayedStart',
            default='false'))
        thread_group_info_dict['scheduler'] = Utils.MAPPING.get(Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path,
            tag='boolProp', 
            name='ThreadGroup.scheduler',
            default='false'))
        thread_group_info_dict['duration'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.duration',
            default='')
        thread_group_info_dict['delay'] = Utils.read_jmxfile_text(
            jmx_path_or_name=plan_jmx_path, 
            tag='stringProp', 
            name='ThreadGroup.delay',
            default='')
        logger.info(thread_group_info_dict)
        return thread_group_info_dict
    
    def get_plan_info(self, plan: str) -> dict:
        """get one plan info"""
        result = dict()
        plan_jmx_path = os.path.join(self.root_dir, plan, 'plan.jmx')
        plan_base_info = self.plan_base_info(plan_jmx_path)
        thread_group_info = self.thread_group_info(plan_jmx_path)
        result.update(plan_base_info)
        result.update(thread_group_info)
        return result