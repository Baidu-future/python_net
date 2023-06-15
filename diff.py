# -*- coding: UTF-8 -*-
"""
File: views
# @Author  : zhoupeifa(zhoupeifa@baidu.com)
"""

import json

class DiffTools(object):
    """
    diff 工具类
    """

    def __init__(self):
        """
        初始化
        """
        pass

    def json_param_diff(self, original_json, compare_json, ignore, check_type=None):
        """
        参数diff
        @original_json:
        @compare_json:
        @ignore:
        """
        if not isinstance(ignore, list):
            ignore = []
   
        if not isinstance(check_type, str):
            check_type = ""

        JsonSchema = check_type.lower() == "JsonSchema".lower()

        if (None is original_json or None is compare_json):
            return "不需要diff校验！"

        diff_body = json_tools.diff(original_json, compare_json)

        replaces, removes, adds= [], [], []
        """组合diff数据"""
        for item in diff_body:
            # 字段存储，数据不一致
            replace = item.get("replace", None)
            if replace is not None:
                if replace not in ignore:
                    value = item.get("value", None)
                    prev = item.get("prev", None)
                    if JsonSchema and type(value) == type(prev):
                        continue
                    replaces.append({
                        "key": replace,
                        "value": value,
                        "prev": prev
                    })
            # 字段被删除
            remove = item.get("remove", None)
            if remove is not None:
                if remove not in ignore:
                    removes.append({
                        "key": remove,
                        #"prev": item.get("prev", None)
                    })
            # 新增字段
            add = item.get("add", None)
            if add is not None:
                if JsonSchema:
                        continue
                if add not in ignore:
                    adds.append({
                        "key": add,
                        "value": item.get("value", None)
                    })
        diff_num = len(replaces) + len(removes)

        body = {
            "diff": {},
            "json": {
                "original_json": json.dumps(original_json, ensure_ascii=False),
                "compare_json": json.dumps(compare_json, ensure_ascii=False)
            },
            "status": True if  diff_num > 0 else False 
        }

        if not JsonSchema:
            body["diff"]["replace"] = replaces
            body["diff"]["add"] = adds

        body["diff"]["remove"] = removes
        
        return body

        

# if __name__ == '__main__':
#     dt = DiffTools()
#     print(json.dumps(dt.json_param_diff(args, args2, check_type="JsonSchema")))
#     pass