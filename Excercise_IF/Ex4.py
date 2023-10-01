gender = str(input("Nhập giới tính của bạn: "))
age = int(input("Nhập tuổi của bạn: "))


if (age >= 65 and gender == "males") or (age >= 60 and gender == "females") :
    print("Eligible Retirements")
else:
    print("No Elogible Retirements")