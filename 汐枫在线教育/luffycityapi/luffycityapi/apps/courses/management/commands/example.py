import random
from django.core.management.base import BaseCommand, CommandError
from courses.models import Teacher
from faker import Faker
from django.conf import settings


# 类名必须是Command而且一个文件就是一个命令类，这个命令类必须直接或间接继承BaseCommand
class Command(BaseCommand):
    help = '添加课程相关的测试数据'

    # 如果当前命令，需要接受来自终端的参数，可以使用add_arguments
    def add_arguments(self, parser):
        # 位置参数，必填项
        # parser.add_argument('name', nargs='+', type=int)

        # 命令参数，可选项
        # parser.add_argument(
        #     '--table',
        #     action='store_true',
        #     help='Delete poll instead of closing it',
        # )

        # 命令参数，可选项
        parser.add_argument(
            '--type',
            dest='type',
            default='teacher',
            type=str,
            help='测试数据的类型',
        )

        parser.add_argument(
            '--number',
            dest='number',
            default=10,
            type=int,
            help='添加数据的数量',
        )

    # 命令执行的核心方法，
    def handle(self, *args, **options):
        """添加课程相关的测试数据"""
        if options["type"] == "teacher":
            self.add_teacher(options)
        elif options["type"] == "direction":
            self.add_direction(options)

    def add_teacher(self, options):
        """添加授课老师的测试数据"""
        faker = Faker(["zh_CN"])
        for i in range(options["number"]):
            Teacher.objects.create(
                name=faker.unique.name(),  # 唯一的姓名
                avatar="teacher/avatar.jpg",
                role=random.randint(0, 2),
                title="老师",
                signature="从业3年，管理班级无数",
                brief=f"从业3年，管理班级无数，联系电话：{faker.unique.phone_number()}，邮箱地址：{faker.unique.company_email()}",
            )
        print("添加授课老师的测试数据完成....")

    def add_direction(self, options):
        """添加学习方向的测试数据"""
        print("添加学习方向的测试数据完成....")
