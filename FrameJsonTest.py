#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
Authors: chenyu(chenyu31@baidu.com)
Description:未经允许，不得转载
Date:  2021-8-28
"""

import json
import yaml
import time
import requests
import numpy
from deepdiff import  DeepDiff
from diff import DiffTools
import pandas as pd


def GetMsgList(loid, size, createtime):
    url_zq = 'https://expert.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList' 
    url_zqd = 'https://expert.baidu.com/wzcui/uiservice/zhenqian/zhusu/getMsgList?isDirected=1&expert_id=1458059' 
    url_zz = 'https://expert.baidu.com/wzcui/uiservice/zhenzhong/chat/getMsgList' 

    headers = {
        'authority': 'expert.baidu.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'BDUSS=DlLRDlRYnNrZVRlV3pLM1lWOEFHQUkwa0JoWE1Wc01LMW54REhnVS1CRDB2ZHhqRVFBQUFBJCQAAAAAAAAAAAEAAAASeaBhQ2hyaXNfY2h1dW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPQwtWP0MLVjb;; BDUSS_BFESS=9GTGNCVDVtZUh3TlFZOUJyU35BTzM2cmxZOUJVZWMwTnpVU1ZCT1VmZ0xDVWhpRVFBQUFBJCQAAAAAAAAAAAEAAAASeaBhQ2hyaXNfY2h1dW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAt8IGILfCBicU',
        'origin': 'https://expert.baidu.com',
        'pragma': 'no-cache',
        'referer': 'https://expert.baidu.com/wenzhen/pages/chat/index?loId=9ca5e5be-9a9e-4e65-8ac6-256ad5a4f0c6_06&lid=2793738385&referlid=3603300559',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    
    payload_zq = json.dumps({
        "page": {
            "size": size,
            "viewType": "pre",
            "msgCreateTime": createtime
        }
    })

    payload_zz = json.dumps({
        "loId": loid,
        "page": {
            "size": size,
            "viewType": "pre",
            "msgCreateTime": "0"
        }
    })

    res_zq = requests.post(url_zq, headers=headers, data=payload_zq).text
    res_zqd = requests.post(url_zqd, headers=headers, data=payload_zq).text
    res_zz = requests.post(url_zz, headers=headers, data=payload_zz).text
    #response = response.headers
    return res_zq, res_zqd, res_zz
    
def makeDiff(res):
    content_list = list()
    json_res = json.loads(res)
    msgData = json_res['data']['msgData']
    #print(msgData)
    for msg_key in msgData:
        #print(msg_key)
        msg_data = msgData.get(str(msg_key), {})
        contentType = msg_data.get("contentType", "")
        if contentType in content_list:
            continue
        else:
            content_list.append(contentType)
            content = msg_data.get("content", "")
            path = "./json/{0}.json".format(contentType)
            try:
                json_file = open(path, 'r', encoding='utf8')
            except Exception as _:
                continue
            #print(json_file)
            original_json = json.load(json_file)
            dt = DiffTools()
            print(contentType)
            result = dt.json_param_diff(original_json, content, ["/data/actionInfo"], check_type="JsonSchema")
            if result['status'] == False:
                print("通过,没有diff")
            else:
                print("存在diff：")
                print(result['diff'])
            print("\n")


if __name__ == '__main__':
    """
    main
    """
    # 读取配置文件
    yamlPath = 'payload.yaml'
    with open(yamlPath, 'r', encoding="utf-8") as f:
        temp = yaml.load(f.read(), Loader=yaml.FullLoader)
    

    # 获取履约单id
    loid = temp['loid']
    size = temp['size']
    createtime = temp['createtime']
    # 执行
    print("开始校验: ")
    res_zq, res_zqd, res_zz = GetMsgList(loid, size, createtime)
    print("诊前非定向：")
    makeDiff(res_zq)
    print("-"*60)
    print("诊前定向：")
    makeDiff(res_zqd)
    print("-"*60)
    print("诊中：")
    makeDiff(res_zz)
    print("-"*60)
    


    # for key in map:
    #     print(key)
    #     value = map.get(key,"")
    #     print(value)
    #     print('-'*100)
    
