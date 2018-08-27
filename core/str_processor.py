# coding:utf-8
'''
此类说明，应能够检测hex字符串，并转为字节串
首先输入的字符串类似：
00 a1 fe 81 ...
字符串应该满足如下条件， 个数为双数， 读入时 无视有无空格， 无视大小写
每个字符应该在0～f之间
'''
import re


class str_processor(object):
    def __init__(self):
        pass
        self.string = None

    def set_string(self, string):
        self.string = string

    def _to_bytes(self):
        hex_list = list()
        for index in range(0, int(len(self.string) / 2)):
            byte = self.string[index * 2:index * 2 + 2]
            hex_list.append(int(byte, 16))
        print(hex_list)
        return bytes(hex_list)

    def _remove_space_upper(self):
        '''
        @func:      删除空白字符,并转换为小写
        @args:      输入字符串类型
        @output:    无空格的大写字符串
        '''
        self.string = re.sub('\s', '', self.string)  # 将string中的所有空白字符删除
        self.string = self.string.upper()

    def _check_string(self):
        '''
        检查是否符合规则
        '''
        pattern = re.compile(r'([0-9A-Fa-f]{2})+')
        m = pattern.match(self.string).group()
        return len(self.string) == len(m)

    def process_string(self, string):
        if isinstance(string, str):
            self.set_string(string)
        if self.string is not None:
            self._remove_space_upper()
            if self._check_string():
                return self._to_bytes()
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    TEST_STR = 'AB CD ED 01  ABBccd'
    s = str_processor()
    print(s.process_string(TEST_STR))
