1. 在Python交互环境中下面的代码查看结果并将内容翻译成中文

```
import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than comples.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the tempation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although never is often better than *right now*.
If the implemetation is hard to explain, it's a bad idea.
If the implematation is easy to explain, it may be a goog idea.
Namesoace are one honking freat idea -- let's do more of those!
```
```
美丽优于丑陋
明确优于含蓄
简单优于复杂
复杂优于更复杂
扁平优于嵌套
稀疏优于密集
可读性最终要
特别情况不足以打破规则
虽然实用性胜过纯净
错误不应该被默默通过
除非明确的标明
面对歧义，拒绝猜想的诱惑
相同的问题应该有且只有一个最优解
尽管这个解在最初不是特别明确，除非你是荷兰人？？？？
现在优于不做
尽管不做大部分情况比现在好
如果实现很难解释清楚，那他可能不是好的想法
如果实现很容易解释清楚，那他就是一个好的想法
命名空间是很好的想法，让我们使用更多的命名空间
```
标准答案

```
优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
 
不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
 
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
 
做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
 
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）
 
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```

1. 学习使用turtle在屏幕上绘制图形。

```python
import turtle

tutle.pensize(4)
tutle.pencolor('red')
tutle.forward(100)
tutle.right(90)
tutle.forward(100)
tutle.right(90)
tutle.forward(100)
tutle.manloop()
```
