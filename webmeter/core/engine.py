import os
import datetime
from loguru import logger
from webmeter.core.utils import Common, Platform
from webmeter.core.sqlhandle import crud
from webmeter.core.task import TaskBase

class EngineServie(TaskBase):

    JMETER_DIR = os.path.join(Common.STATICPATH, 'jmeter', 'apache-jmeter-5.6.2')

    JMETER_PATH = {
        'windows': os.path.join(JMETER_DIR, 'bin', 'jmeter.bat'),
        'macos': os.path.join(JMETER_DIR, 'bin', 'jmeter.sh'),
        'linux': os.path.join(JMETER_DIR, 'bin', 'jmeter.sh')
    }

    @classmethod
    def check_JavaEnvironment(cls):
        result = Common.exec_cmd('java -version')
        if result != 0:
            logger.error('Please download java (https://www.java.com/)')
            raise Exception('No java version found')
        return result    
    
    @classmethod
    def read_JmeterFile(cls, file) -> str:
        file_path = os.path.join(cls.JMETER_DIR, 'bin', file)
        content = Common.read_file_content(file_path)
        return content
    
    @classmethod
    def write_JmeterFile(cls, file, content) -> None:
        file_path = os.path.join(cls.JMETER_DIR, 'bin', file)
        Common.write_file_content(file_path, content)

    @classmethod
    def remote_hosts(cls):
        pass    


    @classmethod
    def run(cls, content: dict, remote=False) -> int:
        """
        execute jmeter command
         -n This specifies JMeter is to run in cli mode
         -t [name of JMX file that contains the Test Plan].
         -l [name of JTL file to log sample results to].
         -j [name of JMeter run log file].
         -r Run the test in the servers specified by the JMeter property "remote_hosts"
         -R [list of remote servers] Run the test in the specified remote servers
         -g [path to CSV file] generate report dashboard only
         -e generate report dashboard after load test
         -o output folder where to generate the report dashboard after load test. Folder must not exist or be empty
            The script also lets you specify the optional firewall/proxy server information:\
         -H [proxy server hostname or ip address]
         -P [proxy server port]
        ex1: jmeter -n -t {jmx_path} 
        ex2: jmeter -n -t {jmx_path} -l {jtl_path} -e -o {report_path} -R 192.168.30.132:1099,192.168.30.130:1099
        """
        task_format = '{}-{}'.format(content.get('plan_name'), datetime.datetime.now().strftime('%y%m%d%H%M%S'))
        report_dir = Common.make_dir(os.path.join(TaskBase.ROOT_DIR, content.get('plan_name'), 'report'))
        log_dir = Common.make_dir(os.path.join(TaskBase.ROOT_DIR, content.get('plan_name'), 'log'))
        report_path = Common.make_dir(os.path.join(report_dir, task_format))
        log_path = Common.make_dir(os.path.join(log_dir, task_format))
        if remote is not True: 
            #单机模式
            crud.create_task(tasks={
                'plan': content.get('plan_name'),
                'task': task_format,
                'model': 'local',
                'threads': int(content.get('threads'))
            })
            result = Common.exec_cmd('{jmeter} -n -t {jmx_path} -l {jtl_path} -j {log_path} -e -o {report_path}'.format(
                jmeter=cls.JMETER_PATH.get(Common.pc_platform()),
                jmx_path=os.path.join(TaskBase.ROOT_DIR, content.get('plan_name'), 'plan.jmx'),
                jtl_path=os.path.join(report_path, 'result.jtl'),
                log_path=os.path.join(log_path, 'result.log'),
                report_path=report_path,
            ))
        else:
            #分布式模式
            result = Common.exec_cmd('{jmeter} -n -t {jmx_path} -l {jtl_path} -j {log_path} -e -o {report_path} -R {hosts}'.format(
                jmeter=cls.JMETER_PATH.get(Common.pc_platform()),
                jmx_path=os.path.join(TaskBase.ROOT_DIR, content.get('plan_name'), 'plan.jmx'),
                jtl_path=os.path.join(report_path, 'result.jtl'),
                log_path=os.path.join(log_path, 'result.log'),
                hosts=content.get('hosts')
            ))
        if result == 0:
            task_result = TaskBase.read_statistics_file(content.get('plan_name'), task_format)
            crud.update_task(tasks={
                'task': task_format,
                'success_num': task_result['Total']['sampleCount'] -  task_result['Total']['errorCount'] ,
                'fail_num': task_result['Total']['errorCount'],
                'status': 'Done'
            })
        else:
            logger.error('task is failed')    
        return result

    @classmethod
    def stop(cls) -> int:
        if Common.pc_platform() == Platform.WINDOWS.value:
            result = Common.exec_cmd(os.path.join(cls.JMETER_DIR, 'bin', 'stoptest.cmd'))
        else:    
            result = Common.exec_cmd(os.path.join(cls.JMETER_DIR, 'bin', 'stoptest.sh'))
        if result != 0:
            logger.error('stop failed')    
        return result
        
class EngineAPI(object):
    """for python api"""
    # 接口：协议、路由、参数
    # 线程数
    # 持续时间
    # JMX文件
    # 测试报告
    # 模式：单机、分布式
    # 是否监控本机性能
    # 配置文件操作
    pass     