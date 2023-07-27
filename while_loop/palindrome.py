# # num=int(input("enter the any num======================="))
# # rem=0
# # temp=0
# # final=0
# # temp=num
# # while num>0:
# #     rem=num%10
# #     num=parseint(num/10)
# #     final=final*10+rem
# #     print("final===========",final)
# #     if final==temp:
# #         print(final,"the input number is a palidrome")
# #     else:
# #         print(final,"this is a not palidrome number")    


# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# print("Palindrome numbers:")
# for num in range(start, end+1):
#     temp = num
#     rev = 0

#     while temp > 0:
#         digit = temp % 10
#         rev = (rev * 10) + digit
#         temp = temp // 10

#     if num == rev:
#         print(num)