import time

start = time.time()
print("30초 세보세요")
print("***************************")
print("마음속으로 30초 세신 후 엔터 누르세요")
print("***************************")

mind = input()
end = time.time()

mind_time = end - start

print("{:.2f}초 지났습니다.".format(mind_time))

if 0 < mind_time - 30 < 1:
    print("빙고! 그냥 살아있는 초시계인데요?")