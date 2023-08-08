import os

class EngineServie(object):

    STATICPATH = os.path.dirname(os.path.realpath(__file__))
    JMETER_PATH = {
        'windows': os.path.join(STATICPATH, 'jmeter', 'win_mac', 'apache-jmeter-5.6.2', 'bin', 'jmeter.bat'),
        'mac': os.path.join(STATICPATH, 'jmeter', 'win_mac', 'apache-jmeter-5.6.2', 'bin', 'jmeter.sh')
    }

    @classmethod
    def set_JmeterPropertiesFile(cls):
        """update jmeter.properties"""
        pass

    @classmethod
    def set_JmeterServerFile(cls):
        """update jmeter-server (sh or bat)"""
        pass

    @classmethod
    def run(cls):
        """
        excute jmeter command
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
        pass