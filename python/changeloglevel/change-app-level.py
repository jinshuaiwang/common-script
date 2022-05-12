#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def get_app_level():
    response = requests.get(url=url)
    return json.loads(response.text)['effectiveLevel']


def change_app_level():
    change_json_data = {"configuredLevel": to_log_level}

    try:
        requests.post(url=url, json=change_json_data)
        print('修改日志输出级别成功')
    except:
        print('修改日志输出级别失败')


if __name__ == '__main__':
    url = 'http://localhost:8080/manage/loggers/file'
    to_log_level = 'ERROR'

    current_log_level = get_app_level()
    print(current_log_level)

    if to_log_level != current_log_level:
        change_app_level()
    else:
        print('日志级别没变,无需修改')
