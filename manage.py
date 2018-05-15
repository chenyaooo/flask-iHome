# coding:utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import create_app, db

app = create_app("develop")


# 创建数据库管理工具
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()




