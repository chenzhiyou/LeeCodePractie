from threading import Lock


class IdMaker:
    """
    懒汉式单例模式
    """
    __instance_lock = Lock()
    __instance = None
    __id = -1

    # 如果__new__抛出异常，就不允许调用者进行实例化
    def __new__(cls):
        raise ImportError("Instantition not allowed")

    # 类方法不用实例化也可以调用，因为我们不允许进行实例化，所以使用类方法
    @classmethod
    def get_instance(cls):
        # 使用简单的线程锁 with会帮我们自动的上锁和释放，不用我们操心
        with cls.__instance_lock:
            if cls.__instance is None:
                #  因为我们的__new__代码不允许实例化，所以可以借用父类的__new__进行实例化
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
    instance_1 = IdMaker.get_instance().get_id()
    instance_2 = IdMaker.get_instance().get_id()
    instance_3 = IdMaker.get_instance().get_id()

    print(instance_1, instance_2, instance_3)


if __name__ == "__main__":
    test_id_maker()
