def marsExploration(s):
    
    error = 0
    for i in range(len(s)):
        if i % 3 == 0:
            # print(i)
            if s[i] != 'S':
                error += 1
            # else:
            #     pass
        if i % 3 == 1:
            # print(i)
            if s[i] != 'O':
                error += 1
            # else:
            #     pass
        if i % 3 == 2:
            # print(i)
            if s[i] != 'S':
                error += 1
            # else:
            #     pass
    return error














# from flask import Flask, url_for
# from flask import request
# from markupsafe import escape
# app = Flask(__name__)


# @app.route("/mars/<text>", methods=["GET"])
# def mars(text):

#     # signal = 'SOSsOsSOs'
#     # length = len(signal)
#     # i,f,key=0,0,''
#     # while i < length/3:
#     #     key = key + 'SOS'
#     #     i=i+1
#     # while i < length:
#     #     if key[i]!=signal[i]:
#     #         f=f+1
#     #     i=i+1
#     # print(f)

#     error = 0
#     for i in range(len(text)):
#         if i % 3 == 0:
#             # print(i)
#             if text[i] != 'S':
#                 error += 1
#             # else:
#             #     pass
#         if i % 3 == 1:
#             # print(i)
#             if text[i] != 'O':
#                 error += 1
#             # else:
#             #     pass
#         if i % 3 == 2:
#             # print(i)
#             if text[i] != 'S':
#                 error += 1
#             # else:
#             #     pass
#     return {
#         "kesalahan": int(error)
#     }
