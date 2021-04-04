site = "http://naver.com"
site1 = site.replace("http://", "")
site2 = site1[:site1.index(".")]
pw = site2[:3] + str(len(site2)) + str(site2.count("e")) + "!"
print(pw)