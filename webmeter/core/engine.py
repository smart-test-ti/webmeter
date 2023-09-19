import os
import datetime
import json
from loguru import logger
from webmeter.core.utils import Common
from webmeter.core.sqlhandle import crud
from webmeter.core.task import TaskBase

class EngineServie(TaskBase):

    JMETER_PATH = {
        'windows': os.path.join(Common.STATICPATH, 'jmeter', 'win_mac', 'apache-jmeter-5.6.2', 'bin', 'jmeter.bat'),
        'macos': os.path.join(Common.STATICPATH, 'jmeter', 'win_mac', 'apache-jmeter-5.6.2', 'bin', 'jmeter.sh')
    }

    @classmethod
    def set_JmeterPropertiesFile(cls) -> None:
        """update jmeter.properties"""
        pass

    @classmethod
    def set_JmeterServerFile(cls) -> None:
        """update jmeter-server (sh or bat)"""
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
            crud.create_task(tasks={
                'plan': content.get('plan_name'),
                'task': task_format,
                'model': 'stand-alone',
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


class EngineAPI(object):
    """for python api"""
    pass     