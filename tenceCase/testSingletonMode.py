
class IdMaker:
    """
    Python的类变量会被多个类，实例共享
    __instance = None
    id也是类变量，多个实例或类共享
    Python在类加载阶段，通过父类的__new__创建实例，如果我们重新__new__，就不会调用父类的__new__，
    就会调用自己写的__new__实例
    重写父类的__new__
    __new__需要返回一个实例，如果不返回，就不会实例化
    """
    __instance = None
    __id = -1

    def __new__(cls):
        if cls.__instance is None:
            # 父类的__new__，参数接收一个类名，会返回类的实例
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_id(self):
        """
        计数器，在获取前，进行+1
        :return:
        """
        self.__id += 1
        return self.__id


def test_id_maker():
    instance_1 = IdMaker().get_id()
    instance_2 = IdMaker().get_id()
    instance_3 = IdMaker().get_id()

    print(instance_1, instance_2, instance_3)


if __name__ == "__main__":
    test_id_maker()
