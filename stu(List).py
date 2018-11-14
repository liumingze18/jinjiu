list=[['jinjiu',18,'python1'],['jinjiu2',19,'python2']]
while True:
	print("======学员管理系统======\n1.查看学员信息  2.添加学员信息\n3.删除学员信息  4.退出系统\n========================\n")
	num=int(input("请输入对应的选择："))
	while num in (1,2,3,4):
		while num==1:
			a=1
			print("======学员信息浏览======\n")
			print("sid  name      age  classid")
			for v1,v2,v3 in list:
				print("{:<5}{:<10}{:<5}{:<}".format(a,v1,v2,v3))
				a+=1
			input("按回车键继续: ")	
			break
			break
		while num==2:
			a=1	
			print("======添加学员信息======\n")
			x=input("请输入学员的姓名： ")
			y=int(input("请输入学员的年龄： "))
			z=input("请输入学员的班级号： ")
			list.append([x,y,z])
			print("sid  name      age  classid")
			for v1,v2,v3 in list:
				print("{:<5}{:<10}{:<5}{:<}".format(a,v1,v2,v3))
				a+=1
			input("学员信息添加成功！按回车键继续: ")
			break
			break	
		while num==3:
			a=1
			print("======删除学员信息======\n")
			print("sid  name      age  classid")
			for v1,v2,v3 in list:
				print("{:<5}{:<10}{:<5}{:<}".format(a,v1,v2,v3))
				a+=1
			num2=int(input("请输入要删除学员信息的序号sid: "))
			list.pop(num2-1)
			a=1
			print("sid  name      age  classid")
			for v1,v2,v3 in list:
				print("{:<5}{:<10}{:<5}{:<}".format(a,v1,v2,v3))
				a+=1
			input("学员信息删除成功！按回车键继续: ")
			break
			break
		while num==4:
			print("======再见！======")
			break
		break
	else:
		print("你输入的参数非法！！！")
