class nodo():
  def __init__(self, value: int, next = None):
    self.value: int = value
    self.next = next

    def __repr__(self):
      return str(self.value)

a = nodo(10)
b = nodo(1)
c = nodo(7)
d = nodo(5)

a.next = b
b.next = c
c.next = d

print(a.value)
print(a.next.value) #Verificar que estén pegados los nodos
print(a.next.next.value) #Brincar al siguiente nodo
print(a.next.next.next.value) #Mostrar el último nodo
print(a.next.next.next.next) #Mostrar el último nodo