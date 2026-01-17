import requests
import time

# 目标URL和请求配置
url = "https://zany-goggles-vp7qg49xg55hw6qj-8000.app.github.dev/submit"
headers = {
    "Content-Type": "application/json",
    "Origin": "https://zany-goggles-vp7qg49xg55hw6qj-8000.app.github.dev/",
}
data = {
    "name":"QQQ","password":"QQQ"
}

# 配置重试参数（应对临时的401/网络问题）
max_retries = 3
retry_delay = 2  # 重试间隔（秒）

# 循环发送请求（添加容错）
while True:
    # 初始化响应变量
    response = None
    try:
        # 带重试机制发送请求
        for retry in range(max_retries):
            try:
                response = requests.post(
                    url,
                    json=data,
                    headers=headers,
                    timeout=10  # 添加超时，避免卡住
                )
                break  # 成功则退出重试循环
            except requests.exceptions.RequestException as e:
                print(f"请求失败（重试 {retry+1}/{max_retries}）：{e}")
                time.sleep(retry_delay)
        else:
            print(f"第{i+1}次请求：多次重试后仍失败，跳过")
            continue

        # 打印状态码
        print(f"第{i+1}次请求 - 状态码：{response.status_code}")

        # 处理响应内容（避免JSON解析失败）
        try:
            # 先检查响应是否非空且是JSON格式
            if response.status_code == 200 and response.text.strip():
                resp_json = response.json()
                print(f"响应内容：{resp_json}")
            else:
                # 非200状态码或空响应，打印原始文本
                print(f"响应内容（非JSON）：{response.text if response.text else '空内容'}")
        except requests.exceptions.JSONDecodeError:
            print(f"JSON解析失败，原始响应：{response.text}")

        # 可选：添加小延迟，避免请求过快被服务器限流
        #time.sleep(0.1)

    except Exception as e:
        # 捕获所有未预期的异常，避免循环中断
        print(f"第{i+1}次请求发生未预期错误：{e}")
        continue