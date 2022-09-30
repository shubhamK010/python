# Slicing of string with jump/skip values

name = " Arnold schwarzenegger is bodybuilding icon "
print(len("name"))
print(name)
print(name[0:8])
# now we have to jump/skip characters so we can use above-
# if we chose 1= we cannot see skipped value
#if we chose 2= we can see skipped by 1 gap
#if we chose 3 = we can see skipped by 2 gap

print(name[0:30:1])
print(name[0:30:2])
print(name[0:30:3])
print(name[0:30:4])
print(name[1:15:2])
print(name[-5:-1])
print(name[-1:-5])   #it gives blank array
print(name[-3:-8])   #it gives blank array


# To study various string methods

himesh1 = '''
O.. huzoor
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
Mere kisse, meri saanein, meri aahein
Tera tera tera suroor
O. huzoor
Tera tera tera suroor
Tujh mein basi hai meri duniya
Tujh mein rawaan hai meri khushiya
Tujh se ummeedein mujhko badi
Todd na dena dil ki kadi
Iss dard ka ehsaas poocho na
Poocho na poocho na, poocho na
Poocho na sanam
Mere armaan, mere lamhe, mere nagme
Tera tera tera suroor
Tanhaiyon mein tu hi shaamil,
Tere bina jeena bada mushkil
Tere siva kuch na aaye nazar
Nazron pe chaaya tera manzar
Rab hi jaane ye pyaas kaisi hai
Dekho na dekho na dekho na
Dekho na sanam
Meri dhadkan, meri tadpan, mera jeevan
Tera tera tera suroor
Meri baatein, meri yaadein, tanha raatein
Tera tera tera suroor
'''

print(himesh1)

print(len(himesh1))

print(himesh1.find("suroor"))#str.find("parameter")gives location of first instance

print(himesh1.count("suroor"))
print(himesh1.count("tera"))

# Methods of uppercase and lowercase

print(himesh1.title())   #It makes first letter of each word in capital letters 
 
print(himesh1.upper())  #It makes complete sentence in capital letters

print(himesh1.swapcase()) #It makes starting letter of every sentence as swap means capital hai to small karega and small hai to capital karega



















