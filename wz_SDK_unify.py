# -*- coding: UTF-8 -*-
"""
@Authors      : v_yuanliangliang
@Date         : 2023-02-24 11:21:00
@LastEditors  : v_yuanliangliang(v_yuanliangliang@baidu.com)
@LastEditTime : 2023-02-24 11:21:00
@Description  : 问诊/搜索策略场景切换统一SDK
@Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved.
"""

import yaml
import requests
import deepdiff
import pprint
import unittest



yamlPath = './payload.yaml'
with open(yamlPath, 'r', encoding="utf-8") as f:
  temp = yaml.load(f.read(), Loader=yaml.FullLoader)
  headers = temp["headers"]


class TestSearchDoctorListSdk(unittest.TestCase):
    def setUp():
        yamlPath = './payload.yaml'
with open(yamlPath, 'r', encoding="utf-8") as f:
  temp = yaml.load(f.read(), Loader=yaml.FullLoader)
  headers = temp["headers"]


  def test_0_1_yishengliebiao(self): # 1.医生列表页老接口
    url_old_yishengliebiao = temp["url_old_yishengliebiao"]   # 1.医生列表页老接口
    payload_old_yishengliebiao = temp["payload_old_yishengliebiao"]
    url_new_yishengliebiao = temp["url_new_yishengliebiao"]  # 医生列表页新接口
    payload1_new_yishengliebiao = temp["payload1_new_yishengliebiao"]
    self.response_old_yishengliebiao = requests.request("GET", url_old_yishengliebiao, headers=headers, data=payload_old_yishengliebiao).json()    #老接口
    self.response1_new_yishengliebiao = requests.request("GET", url_new_yishengliebiao, headers=headers, data=payload1_new_yishengliebiao).json() #新接口
    a = deepdiff.DeepDiff(self.response_old_yishengliebiao, self.response1_new_yishengliebiao)
    pprint.pprint("1.医生列表json比对:")
    pprint.pprint(a['type_changes'])


  def test_0_2_nankezhongxin(self): # 2.男科中心落地页
    url_old_nankezhongxin = temp["url_old_nankezhongxin"]
    payload_old_nankezhongxin = temp["payload_old_nankezhongxin"]
    url_new_nankezhongxin = temp["url_new_nankezhongxin"]
    payload1_new_nankezhongxin = temp["payload1_new_nankezhongxin"]
    response_old_nankezhongxin = requests.request("GET", url_old_nankezhongxin, headers=headers, data=payload_old_nankezhongxin).json()
    response_new_nankezhongxin = requests.request("GET", url_new_nankezhongxin, headers=headers, data=payload1_new_nankezhongxin).json()
    b = deepdiff.DeepDiff(response_old_nankezhongxin,response_new_nankezhongxin)
    print("2.男科中心落地页json比对:")
    pprint.pprint(b["type_changes"])


  def test_0_3_sanwensandayizheng(self):  # 3.三问三答义诊
    url_old_sanwensandayizheng = temp["url_old_sanwensandayizheng"]
    payload_old_sanwensandayizheng = temp["payload_old_sanwensandayizheng"]
    url_new_sanwensandayizheng = temp["url_new_sanwensandayizheng"]
    payload1_new_sanwensandayizheng = temp["payload1_new_sanwensandayizheng"]
    response_old_sanwensandayizheng = requests.request("GET", url_old_sanwensandayizheng, headers=headers, data=payload_old_sanwensandayizheng).json()
    response_new_sanwensandayizheng = requests.request("GET", url_new_sanwensandayizheng, headers=headers, data=payload1_new_sanwensandayizheng).json()
    c = deepdiff.DeepDiff(response_old_sanwensandayizheng,response_new_sanwensandayizheng)
    print("3. 三问三答义诊json比对:")
    pprint.pprint(c)

  def test_0_4_dingxiangIMhuyiqingzixun(self):  #  4.定向IM/互医轻咨询（老）
    url_old_dingxiangIMhuyiqingzixun = temp["url_old_dingxiangIMhuyiqingzixun"]
    payload_old_dingxiangIMhuyiqingzixun = temp["payload_old_dingxiangIMhuyiqingzixun"]
    url_new_dingxiangIMhuyiqingzixun = temp["url_new_dingxiangIMhuyiqingzixun"]
    payload1_new_dingxiangIMhuyiqingzixun = temp["payload1_new_dingxiangIMhuyiqingzixun"]
    response_old_dingxiangIMhuyiqingzixun = requests.request("GET", url_old_dingxiangIMhuyiqingzixun, headers=headers,data=payload_old_dingxiangIMhuyiqingzixun).json()
    response_new_dingxiangIMhuyiqingzixun = requests.request("GET", url_new_dingxiangIMhuyiqingzixun, headers=headers,data=payload1_new_dingxiangIMhuyiqingzixun).json()
    d = deepdiff.DeepDiff(response_old_dingxiangIMhuyiqingzixun,response_new_dingxiangIMhuyiqingzixun)
    print("4.定向IM/互医轻咨询（老）:")
    pprint.pprint(d)


  def test_0_5_dingxiangyisheng(self): # 5. 5041-定向医生
    result = temp["result"]
    result01 = temp["result01"]
    e = deepdiff.DeepDiff(result,result01)
    print("5. 5041-定向医生:")
    pprint.pprint(e)


  def test_0_6_wenyishengka(self): # 6.5192-问医生卡
    old_result_wenyishengka = temp["old_result_wenyishengka"]
    new_result_wenyishengka = temp["new_result_wenyishengka"]
    f = deepdiff.DeepDiff(old_result_wenyishengka,new_result_wenyishengka)
    print("6.5192-问医生卡:")
    pprint.pprint(f)


  def test_0_7_jingxuanyishengzhuanqu(self):# 7.精选医生专区
    url_old_jingxuanyishengzhuanqu = temp["url_old_jingxuanyishengzhuanqu"]
    url_new_jingxuanyishengzhuanqu = temp["url_new_jingxuanyishengzhuanqu"]
    response_old_jingxuanyishengzhuanqu = requests.request("GET", url_old_jingxuanyishengzhuanqu, headers=headers).json()
    response_new_jingxuanyishengzhuanqu = requests.request("GET", url_new_jingxuanyishengzhuanqu, headers=headers).json()
    g = deepdiff.DeepDiff(response_old_jingxuanyishengzhuanqu,response_new_jingxuanyishengzhuanqu)
    print("7.精选医生专区: ")
    pprint.pprint(g)


  def test_0_8_guahaopinpaika(self):#8. 5589-挂号品牌卡
    old_result_guahaopinpaika = temp["old_result_guahaopinpaika"]
    new_result_guahaopinpaika = temp["new_result_guahaopinpaika"]
    h = deepdiff.DeepDiff(old_result_guahaopinpaika,new_result_guahaopinpaika)
    print("8.5589-挂号品牌卡: ")
    pprint.pprint(h)

  def test_0_9_qiangfenzhiyiliuliangwenzhengchonggou(self):
    # 9.千分之一流量-问诊重构
    url_old_qiangfenzhiyiliuliangwenzhengchonggou = temp["url_old_qiangfenzhiyiliuliangwenzhengchonggou"]
    url_new_qiangfenzhiyiliuliangwenzhengchonggou = temp["url_old_qiangfenzhiyiliuliangwenzhengchonggou"]
    response_old_qiangfenzhiyiliuliangwenzhengchonggou = requests.request("GET", url_old_qiangfenzhiyiliuliangwenzhengchonggou, headers=headers).json()
    response_new_qiangfenzhiyiliuliangwenzhengchonggou = requests.request("GET", url_new_qiangfenzhiyiliuliangwenzhengchonggou, headers=headers).json()
    i = deepdiff.DeepDiff(response_old_qiangfenzhiyiliuliangwenzhengchonggou,response_new_qiangfenzhiyiliuliangwenzhengchonggou)
    print("9.千分之一流量-问诊重构:")
    pprint.pprint(i)

  def test_1_0_nankepingpaika(self):  #10.50275-男科品牌卡
    old_result_nankepingpaika = temp["old_result_nankepingpaika"]
    new_result_nankepingpaika = temp["new_result_nankepingpaika"]
    j = deepdiff.DeepDiff(old_result_nankepingpaika,new_result_nankepingpaika)
    print("10.50275-男科品牌卡")
    pprint.pprint(j)

  def test_1_1_CMS_yemian(self):
      print("11.cms页面")


  def test_1_2_zijianye_qianruyishengliebiaoiframe(self): #12.自建页-嵌入医生列表iframe
    url_old_zijianye_qianruyishengliebiaoiframe = temp["url_old_zijianye_qianruyishengliebiaoiframe"]
    url_new_zijianye_qianruyishengliebiaoiframe = temp["url_new_zijianye_qianruyishengliebiaoiframe"]
    response_old_zijianye_qianruyishengliebiaoiframe = requests.request("GET", url_old_zijianye_qianruyishengliebiaoiframe, headers=headers,data=url_new_zijianye_qianruyishengliebiaoiframe).json()
    response_new_zijianye_qianruyishengliebiaoiframe = requests.request("GET", url_old_zijianye_qianruyishengliebiaoiframe, headers=headers,data=url_old_zijianye_qianruyishengliebiaoiframe).json()
    k = deepdiff.DeepDiff(response_old_zijianye_qianruyishengliebiaoiframe,response_new_zijianye_qianruyishengliebiaoiframe)
    print("12.自建页-嵌入医生列表iframe")
    pprint.pprint(k)


  def test_1_3_yiyuantiaozhuanyishengluodiye(self):   #13.医院跳转医生落地页
    url_old_yiyuantiaozhuanyishengluodiye = temp["url_old_yiyuantiaozhuanyishengluodiye"]
    url_new_yiyuantiaozhuanyishengluodiye = temp["url_new_yiyuantiaozhuanyishengluodiye"]
    response_old_yiyuantiaozhuanyishengluodiye = requests.request("GET", url_old_yiyuantiaozhuanyishengluodiye, headers=headers).json()
    response_new_yiyuantiaozhuanyishengluodiye = requests.request("GET", url_new_yiyuantiaozhuanyishengluodiye, headers=headers).json()
    l = deepdiff.DeepDiff(response_old_yiyuantiaozhuanyishengluodiye,response_new_yiyuantiaozhuanyishengluodiye)
    print("13.医院跳转医生落地页")
    pprint.pprint(l)


if __name__=="__main__":
   unittest.main()