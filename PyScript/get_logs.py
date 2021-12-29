import os
import locale
import subprocess


def get_logs(cmd):
    """
    각 운영체제의 CMD창에 명령어를 입력하고, 그 결과를 저장하는 함수입니다.
    파이썬 3.4 이상에서 동작합니다.
    """
    os_encoding = locale.getpreferredencoding()
    #print("System Encdoing :: ", os_encoding)
    if os_encoding.upper() == 'cp949'.upper():  # Windows
        return subprocess.Popen(
            cmd, stdout=subprocess.PIPE).stdout.read().decode('utf-8').strip()
    elif os_encoding.upper() == 'UTF-8'.upper():  # Mac&Linux
        return os.popen(cmd).read()
    else:
        print("None matched")
        exit()
