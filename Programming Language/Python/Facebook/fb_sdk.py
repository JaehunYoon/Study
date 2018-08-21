import facebook
# 생성된 액세스 토큰을 인수로 전달해 사용할 수 있는 객체를 만들어 obj에 저장합니다.
obj = facebook.GraphAPI(access_token="users-token")
limit = int(input("몇건의 게시물을 검색할까요? "))
# facebook객체에서 obj.get_connections함수를 실행시킵니다. get_connections함수는 해당 아이디에서 connection_name으로 전달된 데이터를 가져오는 역할을 합니다. 세 번째 인수로 전달된 limit은 한번에 가져올 게시물의 개수를 정해주는 역할을 합니다. 이 프로그램에서는 id에는 me가 전달되었고 connection_name에는 posts가 전달되었습니다. 결과물은 json으로 반환됩니다.
response = obj.get_connections(id="me", connection_name="posts", limit=limit)
# /me?fields=posts.limit(1)

print(response)

f = open("C:\\Jaehun\\fb.txt", "w")

for data in response["data"]:
    f.write("==" * 30 + "\n")
    f.write("게시물 작성자 : " + str(data["from"]["name"]) + "\n")
    f.write("게시물 아이디 : " + str(data["from"]["id"]) + "\n")
    f.write("최종 업데이트 시간 : " + str(data["updated_time"]) + "\n")
    f.write("게시물 링크 : " + str(data["actions"][0]["link"]) + "\n")
    if "message" in data:
        f.write("게시물 내용 : " + str(data["message"]) + "\n")
    if "picture" in data:
        f.write("게시물 사진 이름 : " + str(data["name"]) + "\n")
        f.write("사진 주소 : " + str(data["picture"]) + "\n")
    if "description" in data:
        f.write("사진 설명 : " + str(data["description"]) + "\n")
    f.write("==" * 30 + "\n")
f.close()