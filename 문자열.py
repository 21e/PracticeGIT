a = "he's a doctor."
print(a)

food = "Python's favorite food is perl."
print(food)

say = "\"Python is very easy.\" he says."
print(say)

multiline = "Life is too short\nYou need python"
print(multiline)


print("%s" % (1+2))

print("=" * 50)
print("Hello")
print("=" * 50)

a = "20160315Sunny"
print(a[-5:])
print(a)


multiline =""" 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
print(multiline)
# 줄바꿈 코드를 사용하는 것이나, 연속된 따옴표를 사용하는 것이나 줄바꿈의 결과는 모두 동일하다.
# 문자열이 여러 줄인 경우 이스케이프 코드(\n)을 사용하는 것보다 따옴표를 연속해서 쓰는 것이 훨씬 깔끔하다.