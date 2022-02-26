"""
demo用于加载不同的文件，对不同的文件做不同的处理
问题：如果创建对象的代码比较多，可能还会创建text等格式
简单工厂解决：把对象的创建移动到其他的类中，load方法就会很简洁
问题：创建实例的代码可能很复杂，简单工厂不能解决，即使迁移到了简单工厂中，复杂的创建过程依旧存在
解决方法：使用工厂方法，把创建过程封装到工厂类
问题：如果存在多个公司，就要封装多个工厂类
解决方法：可以使用抽象工厂解决问题，每个工厂类可以创建多个实例
"""


class Demo:
    def load(self, rule):
        parse = ParseRuleFactory().create_parse(rule)
        # 调用对象的方法进行不同操作
        parse.parse()


class ParseRuleFactory:
    def create_parse(self, rule):
        parse = None
        # 根据不同的rule，创建不同的对象，根据rule创建不同的实例，本质就是把Demo中原来创建实例的代码，给迁移过来
        if "xml" == rule:
            parse = XmlParse()
        elif "excel" == rule:
            parse = ExcelParse()
        elif "json" == rule:
            parse = JsonParseRuleFactory().create_parse()
        elif "csv" == rule:
            parse = CsvParse()
        else:
            parse = OtherParse()
        return parse


# 相当于接口，用于规范各个工厂类
class IParseRuleFactory:
    def create_parse(self):
        raise ValueError()


# 工厂：把JSON的解析放到此工厂下面
class JsonParseRuleFactory(IParseRuleFactory):
    def create_parse(self):
        return JsonParse()


# 相当于接口，用于规范各个解析类，每个解析类都要实现parse方法
class IParse:
    def parse(self):
        raise ValueError()


class XmlParse(IParse):
    def parse(self):
        print("XmlParse")


class ExcelParse(IParse):
    def parse(self):
        print("ExcelParse")


class JsonParse(IParse):
    def parse(self):
        print("JsonParse")


class CsvParse(IParse):
    def parse(self):
        print("CsvParse")


class OtherParse(IParse):
    def parse(self):
        print("OtherParse")


if __name__ == "__main__":
    Demo().load("json")
