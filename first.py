#simple.py
# languages = ['python','perl','C','java']
# for lang in languages:
#     if lang in['python','perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in['C','java']:
#         print("%6s need compiler"%lang)
#     else:
#         print("should not reach here")

#<기본문>        
# a = "python"
# print(a)


# <조건문>
# a = 3
# if a > 1:
#     print("a is greater than 1")
    
# #<for 반복문>
# for a in[1,2,3]:
#     print(a)


#<while 반복문>
# i = 0
# while i < 3:
#     i=i+1
#     print(i)     #i가 0일때 1....i가 2일때 3으로 i값이 3보다 커지면 while문 탈출
    


#<함수>
# def add(a,b):           #def는 예약어, add함수에 a,b는 입력값
#     return a+b          #결과값 3,4
# print(add(3,4))                 #7을 반환해줌                                      
       

# a = 0o1077
# b = 0xABC



# multistring.py <문자열 곱하기 응용하기 >
# print("="*50)
# print("My Program")
# print("="*50)



#<문자열 길이 구하기>
# a = "Life is too short"
# print(len(a))


#<문자열 인덱싱과 슬라이싱>
a = "Life is too short, You need Python"
print(a[3])
