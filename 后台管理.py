import os
import requests
if os.path.isfile("settings.ini"):
	settingsf = open("settings.ini","r+",encoding="utf-8")
	settings = settingsf.read()
	settingsf.close()
	settings = settings.split("\n")
	urla = settings[1]
	key = settings[3]
	servername = settings[5]
	qqlistfilepath = settings[7]
	autoexitaddblack = settings[9]
else:
	file = open("settings.ini","a+",encoding="utf-8")
	file.write("这里为你需要提交url 如果非80 443等默认端口 则需要在添加端口号 请保留http或https url结尾不要加多余的成分 即使是“/”\nsimple.test.org:11451\n这里为你的提交post请求所需要的key\n123456abcdefg\n这里为你所需要的发出请求的服务器名称\nBE_Survive\n你的qq列表 已使用换行切分的文件在哪里\n./qqlist.txt\n群员退群后是否加入黑名单\nTrue")
	file.close()
	print("你似乎没有配置文件 请根据程序生成的默认配置及其提示进行修改")
def createwhite():
	id = str(input("id:"))
	qq = str(input("qq:"))
	filename = qq + ".txt"
	res = id
	file = open("nowwhitelist/" + filename,"w+",encoding="utf-8")
	file.write(res)
	file.close()
	command = "whitelist add \"" + id + "\""
	try:
		requests.post(url=urla + '/api/execute/?apikey=' + key,data={'name':servername,'command':command},headers={'Content-Type':'application/x-www-form-urlencoded'})
		print("已成功提交")
	except Exception as e:
		print(e.__class__.__name__,e)

def list():
	filelist = os.listdir("./nowwhitelist/")
	for i in filelist:
		nf = "./nowwhitelist/"+i
		fo = open(nf, "r+", encoding="utf-8")
		c = fo.readlines()
		for c in c:
			print(c)
		print("\n")

def black():
	filelist = os.listdir("nowwhitelist/")
	id = str(input("id:"))
	for i in filelist:
		nf = "nowwhitelist/"+i
		fo = open(nf, "r+", encoding="utf-8")
		c = fo.readlines()
		for nc in c:
			nc = nc.replace("\n","")
			if id == nc:
				qq = i.replace(".txt","")
				file = open("blackqq.txt","a+",encoding="utf-8")
				file.write(qq + "\n")
				file.close()
				file = open("blackid.txt","a+",encoding="utf-8")
				file.write(id + "\n")
				file.close()
				fo.close()
				os.remove(nf)
				command = "whitelist remove \"" + id + "\""
				try:
					requests.post(url=urla + '/api/execute/?apikey=' + key,data={'name':servername,'command':command},headers={'Content-Type':'application/x-www-form-urlencoded'})
					print("成功移除白名单并添加至黑名单")
				except Exception as e:
					print(e.__class__.__name__,e)

def remove():
	filelist = os.listdir("nowwhitelist/")
	id = str(input("id:"))
	for i in filelist:
		nf = "nowwhitelist/"+i
		fo = open(nf, "r+", encoding="utf-8")
		c = fo.read()
		if id == c:
			qq = i.replace(".txt","")
			fo.close()
			os.remove(nf)
			command = "whitelist remove \"" + id + "\""
			try:
				requests.post(url=urla + '/api/execute/?apikey=' + key,data={'name':servername,'command':command},headers={'Content-Type':'application/x-www-form-urlencoded'})
				print("成功移除白名单")
			except Exception as e:
				print(e.__class__.__name__,e)

def search():
	uid = str(input("输入id的部分："))
	filelist = os.listdir("./nowwhitelist/")
	for i in filelist:
		nf = "./nowwhitelist/"+i
		fo = open(nf, "r+", encoding="utf-8")
		id = fo.read()
		qq = i.replace(".txt","")
		result = uid in id
		if result:
			print("=======================\n" + id + "\n" + qq + "\n=======================")


xunhuan = int(0)
while xunhuan < 1:
	print("输入编号进行一系列操作\n1）加入白名单\n2）列出所有白名单\n3）移除白名单并添加至黑名单\n4）输入id的部分查qq\n5）移除白名单但是不添加至黑名单\n=========================")
	chose = input("请输入编号：")
	if chose == "1":
		createwhite()
	elif chose == "2":
		list()
	elif chose == "3":
		black()
	elif chose == "4":
		search()
	elif chose == "5":
		remove()