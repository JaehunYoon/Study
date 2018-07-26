class ChanError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

# try:
#     int('python')
# except NameError as e:
#     print(e)
#     print(type(e))
# except ValueError as e:
#     print(e)
#     print(type(e))
try:
    if 1:
        raise ChanError('오류야 나타나줘 ~')
except ChanError as e:
    print(e)
