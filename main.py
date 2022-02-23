peso =float (input ("introdusca peso"))
estatura = float (input ("introdusca estatura"))
imc = peso / estatura ** 2
if imc < 16.0:
	print ("Underweight (Severe thinness)")
elif imc >= 16.0 and imc <= 16.9:
	print ("Underweight (Moderate thinness)")
elif 17.0 <= imc <= 18.4:
	print("Underweight (Mild thinness)")
elif 18.5 <= imc <= 24.9:
	print("Normal range")
elif 25.0 <= imc <= 29.9:
	print("Overweight (Pre-obese)")
elif 30.0 <= imc <= 34.9:
	print("Obese (Class I)")
elif 35.0 <= imc <= 39.9:
	print("Obese (Class II)")
else:
	print("ya bajale a los tacos de doña pelos")


