import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from common.libs.UrlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(
            import_name,
            template_folder=template_folder,
            root_path=None,
            static_folder=None
        )
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])

        db.init_app(self)


db = SQLAlchemy()
app = Application(
    __name__,
    template_folder=os.getcwd() + '/web/templates/',
    root_path=os.getcwd()
)
manager = Manager(app)

'''
模板函数
'''
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')
