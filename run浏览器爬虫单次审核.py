import os
import re
import requests
import time
def scroll_foot(driver):
	js="var q=document.documentElement.scrollTop=100000"
	return driver.execute_script(js)
x = 0
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
	x = 1
	file = open("settings.ini","a+",encoding="utf-8")
	file.write("这里为你需要提交url 如果非80 443等默认端口 则需要在添加端口号 请保留http或https url结尾不要加多余的成分 即使是“/”\nsimple.test.org:11451\n这里为你的提交post请求所需要的key\n123456abcdefg\n这里为你所需要的发出请求的服务器名称\nBE_Survive\n你的qq列表 已使用换行切分的文件在哪里\n./qqlist.txt\n群员退群后是否加入黑名单\nTrue")
	file.close()
	print("你似乎没有配置文件 请根据程序生成的默认配置及其提示进行修改")
if os.path.isfile("se.ini"):
	sef = open("se.ini","r+",encoding="utf-8")
	se = sef.read()
	sef.close()
	se = se.split("\n")
	qqgroup = se[1]
	executablepath = se[3]
else:
	x = 1
	file = open("se.ini","a+",encoding="utf-8")
	file.write("输入你的qq群群号\n1145141919810\n输入geckoddriver位置\nC:\\Users\\Lendwishes\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\geckodriver.exe")
	file.close()
	print("你似乎没有爬虫配置文件 请根据程序生成的默认配置及其提示进行修改")
if x < 1:
	from selenium import webdriver
	spider = str(input("是否需要刷新成员名单 直接回车需要 输入1并回车表示不需要"))
	if spider == "":
		group_id = qqgroup ##群号
		url = 'https://qun.qq.com/member.html#gid={}'.format(group_id)
		driver = webdriver.Firefox(executable_path = executablepath) 
		driver.get(url=url)
		time.sleep(10)
		max_n = 0
		while max_n < len(driver.page_source):
			max_n = len(driver.page_source)
			scroll_foot(driver)
			time.sleep(2.5)
		res = driver.page_source
		out = open("download.html","w",encoding="utf-8")
		out.write(str(res))
		out.close()
		driver.quit()
		log = open("download.html", "r+", encoding="utf-8")
		res = log.readlines()
		qqlist = ""
		for ares in res:
			srobj = re.search( r'mb mb(.*)\"', ares, re.M|re.I)
			if srobj:
				qqlist = qqlist + srobj.group().replace("mb mb","").replace("\"","") + "\n"
		print(str(qqlist))
		qqlistf = open("qqlist.txt", "w+", encoding="utf-8")
		qqlistf.write(qqlist)
		qqlistf.close()
	log = open("log.log","a+",encoding="utf-8")
	qqlistf = open(qqlistfilepath, "r+", encoding="utf-8")
	qqlist = qqlistf.read()
	qqlistf.close()
	qqlistlist = qqlist.split("\n")
	filelist = os.listdir("./nowwhitelist/")
	for i in filelist:
		nf = "./nowwhitelist/"+i
		fo = open(nf, "r+", encoding="utf-8")
		c = fo.readlines()
		fo.close()
		a =  0
		for xhnr in c:
			xhnr = xhnr.replace("\n","")
			if a == 0:
				id = xhnr
				a = 1
			if a == 1:
				qq = i.replace(".txt","")
				result = False
				for nqq in qqlistlist:
					if qq == nqq:
						result = True
				if result:
					pass
				else:
					print("=================================================")
					log.write("=================================================\n")
					print(id)
					log.write(id + "\n")
					print(qq)
					log.write(qq + "\n")
					command = "whitelist remove \"" + id + "\""
					try:
						requests.post(url=urla + '/api/execute/?apikey=' + key,data={'name':servername,'command':command},headers={'Content-Type':'application/x-www-form-urlencoded'})
						if autoexitaddblack == "True":
							file = open("blackqq.txt","a+",encoding="utf-8")
							file.write(qq + "\n")
							file.close()
							file = open("blackid.txt","a+",encoding="utf-8")
							file.write(id + "\n")
							file.close()
							fo.close()
						try:
							os.remove(nf)
						except Exception as e:
							print(e.__class__.__name__,e)
						print("玩家因不在群内而被移除白名单")
						print("=================================================")
						log.write("玩家因不在群内而被移除白名单" + "\n")
						log.write("=================================================" + "\n")
					except Exception as e:
						print(e.__class__.__name__,e)
	waitlistfist = os.listdir("./waitfor/")
	if str(waitlistfist) == "[]":
		pass
	else:
		for waitfilename in waitlistfist:
			if waitfilename == ".txt":
				pass
			else:
				print("=================================================")
				log.write("=================================================" + "\n")
				nowwaitfilepath = "./waitfor/" + waitfilename
				nowwaitfile = open(nowwaitfilepath,"r+",encoding="utf-8")
				nowwaitfileconcertlist = nowwaitfile.readlines()
				id = nowwaitfileconcertlist[0].replace("\n","")
				qq = nowwaitfileconcertlist[1]
				ok = True
				qqblackfile = open("blackqq.txt", "r+", encoding="utf-8")
				qblline = qqblackfile.readlines()
				for nqq in qblline:
					nqq = nqq.replace("\n","")
					if qq == nqq:
						ok = False
						log.write("你在qq的黑名单当中" + "\n")
						print("你在qq的黑名单列表当中")
				qqblackfile.close()
				idblackfile = open("blackid.txt", "r+", encoding="utf-8")
				iblline = idblackfile.readlines()
				for nid in iblline:
					nid = nid.replace("\n","")
					if id == nid:
						ok = False
						log.write("你在id的黑名单当中" + "\n")
						print("你在id的黑名单当中")
				idblackfile.close()
				qqlistf = open(qqlistfilepath,"r+",encoding="utf-8")
				qqlist = qqlistf.readlines()
				qqlistf.close()
				cunzai = False
				for nqq in qqlist:
					nqq = nqq.replace("\n","")
					if nqq == qq:
						cunzai = True
				if cunzai:
					pass
				else:
					ok = False
					log.write("输入的qq不在群内，请检查qq是否在寻内或数据是否更新" + "\n")
					print("输入的qq不在群内，请检查qq是否在寻内或数据是否更新")
				filelist = os.listdir("./nowwhitelist/")
				for i in filelist:
					nf = "./nowwhitelist/"+i
					fo = open(nf, "r+", encoding="utf-8")
					c = fo.readlines()
					fo.close()
					for aaa in c:
						aaa = aaa.replace("\n","")
						if id == aaa:
							log.write("id已被占用" + "\n")
							print("id已被占用")
							ok = False
				filelist = os.listdir("./nowwhitelist/")
				for i in filelist:
					nf = "./nowwhitelist/"+i
					fo = open(nf, "r+", encoding="utf-8")
					c = fo.readlines()
					fo.close()
					for aaa in c:
						aaa = aaa.replace("\n","")
						if qq == aaa:
							log.write("qq已被占用" + "\n")
							print("qq已被占用")
							ok = False
				if ok:
					print("符合要求，正在添加至白名单")
					log.write("符合要求，正在添加至白名单" + "\n")
					filename = qq + ".txt"	
					res = id
					file = open("nowwhitelist/" + filename,"w+",encoding="utf-8")
					file.write(res)
					file.close()
					command = "whitelist add \"" + id + "\""
					try:
						requests.post(url=urla + '/api/execute/?apikey=' + key,data={'name':servername,'command':command},headers={'Content-Type':'application/x-www-form-urlencoded'})
					except Exception as e:
						print(e.__class__.__name__,e)
					print("ID:" + id + "\nQQ:" + qq)
					log.write("ID:" + id + "\nQQ:" + qq + "\n")
					time.sleep(1)
				else:
					print("ID:" + id + "\nQQ:" + qq)
					log.write("ID:" + id + "\nQQ:" + qq + "\n")
					print("不符合要求 请查看上述信息寻求帮助")
					log.write("不符合要求 请查看上述信息寻求帮助" + "\n")
				nowwaitfile.close()
				os.remove(nowwaitfilepath)
				log.write("=================================================" + "\n")
				print("=================================================")
	log.close()
	##print("==============================================================")
	time.sleep(10)
