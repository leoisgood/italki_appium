import os
import time
import pytest
current = os.path.dirname(__file__)
json_report_path = os.path.join(current, 'reports', 'json_report')
html_report_path = os.path.join(current, 'reports', 'html_report', time.strftime('%Y_%m_%d_%H%M%S'))
if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
    os.system( 'allure generate %s -o %s --clean' % (json_report_path, html_report_path) )
