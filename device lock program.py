print("My name is rizwan and this is to check the python code")
print("this program is written for demonstration of simple cheking of something")
print("========================================================================")
print("************************************************************************")
print("========================================================================")
print("Enter username and password to unlock the program: ")
print("---------------------------------------------------")
user=input("Please Enter the Username  : ")
print("---------------------------------------------------")
passwd=input("Please Enter the Password : ")
print("---------------------------------------------------")
username='rizwan'
password='123'
if user==username and password==passwd:
	print(" Device unlocked successfully .........")
	print("Now you can use the device.............")
	print("Thankyou for using this program")
else :
	print("Wrong user name or password.......")
	print("Please try again later....")
	print("Bye bye i do not recognise you")
print("Thankyou for using this program")
print("---------------------------------------------------")
print("========================================================================")
print("************************************************************************")
print("========================================================================")
import matplotlib.pyplot as plt  
import matplotlib.animation
firstcircle = int(input("please input radius for the largest circle"))
secondcircle = int(input("please input radius for the adjacent circle"))
largest = int(firstcircle*2+secondcircle*2)
difference = int(0-(largest))
difference2 = int(0+(largest))


def createList(r1, r2):
    return [item for item in range(r1, r2+1)]


x = (createList(difference,difference2))
y = (createList(difference,difference2))

print(difference)
print(difference2)


def circle():
  theta = np.linspace(0, 2*np.pi, 100)

  r = np.sqrt(firstcircle**2)

  x1 = r*np.cos(theta)
  x2 = r*np.sin(theta)

  theta2 = np.linspace(0, 2*np.pi, 100)
  r1 = np.sqrt(secondcircle**2)
  x3 = r1*np.cos(theta2)+firstcircle+secondcircle
  x4 = r1*np.sin(theta2)

  fig = plt.figure()

  ax = fig.add_subplot(1, 1, 1)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  ax.plot(x1,x2)
  circlemove ,= ax.plot(x3,x4)  

  ax.set_aspect(1)
  plt.tight_layout()

  plt.xlim(difference,difference2)
  plt.ylim(difference,difference2)


  plt.grid(linestyle='--')

  plt.show()

circle()
