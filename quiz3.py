site = "http://naver.com"
site1 = site.replace("http://", "")
site2 = site1[:site1.index(".")]
pw = site2[:3] + str(len(site2)) + str(site2.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(site, pw))
