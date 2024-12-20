class ClassCPU:
	def __init__(self):
		self.memory=[0] * 256 # Simula a memória com 256 posições. 
		self.accumulator = 0 # Registrador acumulador
	def load_to_memory(self, value, address):
		# Lacuna 1: Carregar um valor na memória no endereço especificado. 
		pass

	def fetch(self, address):
		#Lacuna 2: Retornar o valor do endereço de memória especificado. 
    pass

  
  def load_to_accumulator(self,value):
  #Lacuna 3: Carregar um valor no acumulador. 
    pass

  def execute(self, op, mem_address): 
    memory_value=self.fetch(mem_address) 
    if op == 'add':
      #Lacuna 4: Adicionar o valor da memória ao acumulador. 
      pass
    elif op=='sub':
      #Lacuna: Subtrair o valor da memória do acumulador. 
      pass
    elif op=='mul':
      #Lacuna 6:Multiplicar o acumulador pelo valor da memória.
      pass
    elif op=='div':
      if memory_value != 0:
        #Lacuna 7:Dividir o acumulador pelo valor damemória. 
        pass
      else:
        print("Erro: Divisão por zero") 
    elif op == 'neg':
      #Lacuna 8: Inverter o sinal do acumulador. 
      pass

  def run(self):
    initial_value=int(input("Digite o valor inicial para o acumulador: ")) 
    self.load_to_accumulator(initial_value)
    mem_address=int(input("Digite o endereço de memória: ")) 
    op = input("Escolha a operação (add, sub, mul, div, neg): ") 
    self.execute(op, mem_address)
    print(f'Resultado no acumulador= {self.accumulator}')

if __name__ =="__main__":
	cpu = ClassCPU()
