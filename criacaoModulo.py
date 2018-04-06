#Além de utilizar módulos prontos, o python permite criar seus próprios módulos

import modulo

print(modulo.media(2,3))
print(modulo.multiplicacao(5,2))
print(modulo.potencia(60,20))

from modulo import * # Import universal

print(media(7,2))
print(multiplicacao(15,20))
print(potencia(6540,20))