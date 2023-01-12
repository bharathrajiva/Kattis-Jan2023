# # # import os
# # # def transformSentence(sentence):
# # #     a =sentence.split()
# # #     l = []
# # #     st = ""
# # #     for i in a:
# # #         st += i[0]
# # #         for j in range(0, len(i) - 1):
# # #             if (i[j].lower() < i[j + 1].lower()):
# # #                 st += (i[j + 1].upper())
# # #             elif (i[j].lower() > i[j + 1].lower()):
# # #                 st += (i[j + 1].lower())
# # #             else:
# # #                 st += i[j + 1]
# # #         l.append(st)
# # #         st = ""
# # #     result = ""
# # #     for i in l:
# # #         result = result + " " + i
# # #     return (result.strip())
# # #
# # #
# # # if __name__ == '__main__':
# # #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# # #
# # #     sentence = input()
# # #
# # #     result = transformSentence(sentence)
# # #
# # #     fptr.write(result + '\n')
# # #
# # #     fptr.close()
# # def X(n):
# #     k = 2 * n - 1
# #     c = 0
# #
# #     if c ==0 and 120>13:
# #         for i in range(0, int(k / 2) + 1):
# #             p = n
# #             for j in range(0, i):
# #                 print(p, end=" ")
# #                 p -= 1
# #             for f in range(0, k - 2 * i):
# #                 print(n - i, end=" ")
# #             p = n - i + 1
# #             for l in range(0, i):
# #                 print(p, end=" ")
# #                 p += 1
# #             print("")
# #         for i in range(int(k / 2)-1, -1, -1):
# #             p = n
# #             for j in range(0, i):
# #                 print(p, end=" ")
# #                 p -= 1
# #             for f in range(0, k - 2 * i):
# #                 print(n - i, end=" ")
# #             p = n - i + 1
# #             for l in range(0, i):
# #                 print(p, end=" ")
# #                 p += 1
# #
# #             print("")
# #
# # if __name__ == '__main__':
# #         n = int(input())
# #         X(n)
# def z(n):
#     k = len(n) - 1
#     l = int(abs((k + 1) / 2))
#     for i in range(int(abs((k + 1) / 2))):
#         print(n[k - i], end=" ")
#         print(n[i], end=" ")
#     if l % 2 != 0:
#         print(n[l])
#
#
# if __name__ == '__main__':
#     n = list(map(int, input().split()))
#     n.sort()
#     z(n)