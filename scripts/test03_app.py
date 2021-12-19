from api.api_app import ApiApp
from tools.get_log import GetLog
from tools.tools import Tools
log = GetLog().get_logger()


class TestApp:
    # 1、初始化
    def setup_class(self):
        # 获取ApiApp对象
        self.app = ApiApp()

    # 2、登录测试接口
    def test01_app_login(self, mobile="13911111111", code="246810"):
        # 1、调用登录接口
        r = self.app.api_app_login(mobile, code)
        # 2、提取token
        Tools.common_token(r)
        try:
            # 3、断言
            Tools.common_assert(r)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

    # 3、查询频道下所有文章测试接口
    def test02_app_article(self):
        # 1、调用查询接口
        r = self.app.api_app_article()
        try:
            # 2、断言
            Tools.common_assert(r, status_code=200)
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise

