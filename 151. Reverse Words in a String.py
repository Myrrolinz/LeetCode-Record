class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        # print(word_list)
        # 注意两个用法：split和join
        # .split() 方法用于将字符串按照指定的分隔符拆分成一个列表。如果不指定分隔符，方法默认会以所有的空白字符（包括空格、换行 \n、制表符 \t 等）作为分隔符来分割字符串。
        # join() 方法是一个字符串方法，用于将序列中的元素（序列中的元素必须是字符串）通过指定的字符串连接成一个新的字符串。
        word_list.reverse()
        return ' '.join(word_list)
