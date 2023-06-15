import os

# 定义相册应用程序的包名
album_package_name = "com.vivo.gallery"

# 打开相册
os.system(f"am start -n {album_package_name}/.app.GalleryActivity")
import time
import uiautomator2 as u2

# 连接到设备
d = u2.connect()

# 启动Vivo相册应用程序
d.app_start("com.android.gallery3d")

# 如果是Vivo S5，可能需要单击"进入相册"按钮
if d(resourceId="com.android.gallery3d:id/confirm_button").exists():
    d(resourceId="com.android.gallery3d:id/confirm_button").click()

# 等待相册加载完成
time.sleep(2)

# 点击选择按钮
if d(resourceId="com.android.gallery3d:id/action_select").exists():
    select_button = d(resourceId="com.android.gallery3d:id/action_select")
    select_button.click()

# 等待弹窗出现
time.sleep(2)

# 点击相册选择弹窗的确认按钮
if d(resourceId="com.android.gallery3d:id/ok").exists():
    ok_button = d(resourceId="com.android.gallery3d:id/ok")
    ok_button.click()

# 断开设备连接
d.disconnect()
