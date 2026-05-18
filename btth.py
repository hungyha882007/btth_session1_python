import random
name = input("nhập tên bệnh nhân :");
gender = input("nhập giới tính :");
birth_year = int(input("nhập năm sinh bệnh nhân :"));
phone = int(input("nhập số điện thoại :"));
email = input("nhập email :");
symptom = input("nhập triệu chứng ban đầu :");
cost = int(input("nhập chi phí :")); 

id_patient ="BN" + str(birth_year) + str(random.randint(100,999))


print("--- THẺ BỆNH NHÂN ---");
print(f"tên bệnh nhân {name}");
print(f"giới tính{gender}");
print(f"năm sinh{birth_year}");
print(f"số điện thoại{phone}");
print(f"email{email}");
print(f"triệu chứng{symptom}");
print(f"chi phí {cost}");
