import requests
import os
import shutil
# img_url = 'https://i.imgur.com/fItKbmc.jpg'
# response = requests.get(img_url)
# print(response.status_code)
# if response.status_code:
#     fp = open('greenland_01a.jpg', 'wb')
#     fp.write(response.content)
#     fp.close()

# print(response.content == open("greenland_01a.jpg","rb").read())

PATH = r".\nsfw_data_source_urls-master\raw_data"
for i in os.listdir(PATH):
    for j in os.listdir(PATH + "\\" + i):
        if ".txt" not in j:
            shutil.rmtree(PATH + "\\" + i + "\\"+j)

for i in os.listdir(PATH):
    for j in os.listdir(PATH + "\\" + i):
        count = ind = 0
        if not(os.path.exists("New_data\\"+ i)):
            os.mkdir("New_data\\"+ i)
        src = open(PATH + "\\" + i + "\\"+j)
        s = src.readlines()
        while(count<50):
            img_url = s[ind].strip()
            try:
                response = requests.get(img_url)
            except:
                ind+=1
                continue
            if response.status_code:
                fp = open("New_data\\"+ i + "\\nude" + str(count) + ".jpg", 'wb')
                fp.write(response.content)
                fp.close()
                if os.path.getsize("New_data\\"+ i + "\\nude" + str(count) + ".jpg") <= 130000:
                    os.remove("New_data\\"+ i + "\\nude" + str(count) + ".jpg")
                    count-=1
            count+=1
            ind += 1
    print("Folder Done")


print(len(os.listdir(PATH)))