import matplotlib.pyplot as plt
meses = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho']
vendas = [200,300,340,305,360,400]
plt.plot(meses, vendas)
plt.title("vendas do primeiro semestre")
plt.xlabel("meses")
plt.ylabel("vendas")
plt.show()
