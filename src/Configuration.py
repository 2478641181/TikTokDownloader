import json
import os


class Settings:
    def __init__(self):
        self.file = "./settings.json"  # 配置文件
        self.__default = {
            "accounts": [
                ["", "https://v.douyin.com/XXXXXXX/", "post", "2016/9/20", ""],
            ],
            "root": "./",
            "folder": "Download",
            "name": "create_time nickname desc",
            "time": "%Y-%m-%d %H.%M.%S",
            "split": "-",
            "music": [False, ],  # 单线程模式仅第一个值生效，多线程模式按索引对应的账号生效
            "save": "",
            "cookie": ["", ],  # 单线程模式仅第一个值生效，多线程模式按索引对应的账号生效
            "dynamic": [False, ],  # 单线程模式仅第一个值生效，多线程模式按索引对应的账号生效
            "original": [False, ],  # 单线程模式仅第一个值生效，多线程模式按索引对应的账号生效
            "proxies": ["", ],  # 单线程模式仅第一个值生效，多线程模式按索引对应的账号生效
            "log": False,  # 是否启用日志
            "download": [True],  # 是否启用下载功能
            "retry": 10,  # 重试最大次数
        }  # 默认配置

    def create(self):
        """创建默认配置文件"""
        with open(self.file, "w", encoding="UTF-8") as f:
            json.dump(self.__default, f)
        print("创建默认配置文件成功，请修改“settings.json”文件后重新运行程序！")

    def read(self):
        """读取配置文件，如果没有配置文件，则生成配置文件"""
        try:
            if os.path.exists(self.file):
                with open(self.file, "r", encoding="UTF-8") as f:
                    return json.load(f)
            else:
                print("配置文件读取失败，文件不存在！")
                self.create()
                return False  # 生成的默认配置文件必须要设置cookie才可以正常运行
        except json.decoder.JSONDecodeError:
            return {}  # 读取配置文件发生错误时返回空配置

    def update(self, settings: dict):
        """更新配置文件"""
        with open(self.file, "w", encoding="UTF-8") as f:
            json.dump(settings, f)
        print("保存配置成功！")


if __name__ == "__main__":
    print(Settings().read())
