# Practice BMI calculation
# BMI = weight(kg) / height (m)^2

weight = input('請輸入體重(kg)： ')
weight = int(weight)
height = input('請輸入身高(m)： ')
height = float(height)
bmi = weight / (height) ** 2

if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重適中')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
