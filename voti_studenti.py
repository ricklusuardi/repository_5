from random import randint

voti_Enzo=[]

voti_Nunzio=[]

voti_insuf_Enzo=[]

voti_insuf_Nunzio=[]

print('')
n_Enzo=float(input('Quanti voti ha Enzo? '))

print('')

n_Nunzio=float(input('Quanti voti ha Nunzio? '))

print('')

a=0

while a<n_Enzo:

	print('')
	voto_inserire=float(input('inserisci il voto di Enzo '))
	voti_Enzo.append(voto_inserire)

	if voto_inserire<6:

		voti_insuf_Enzo.append(voto_inserire)

	a= a+1

print('')

a=0

while a<n_Nunzio:

	print('')

	voto_inserire=float(input('inserisci il voto di Nunzio '))
	voti_Nunzio.append(voto_inserire)

	if voto_inserire<6:

		voti_insuf_Nunzio.append(voto_inserire)

	a=a+1

print('')
nome=input('scriva il nome dello studente di cui vuole vedere i voti: ')

while nome!="Enzo" and nome!="Nunzio":

	print('')
	nome=input('Il nome dello studente è errato, riprovare (ricorda la prima lettera maiuscola!): ')

somma_Enzo=0

for i in voti_Enzo:

	somma_Enzo=somma_Enzo + i

	lunghezza_Enzo=len(voti_Enzo)

	media_Enzo= somma_Enzo/lunghezza_Enzo

somma_Nunzio=0

for i in voti_Nunzio:

	somma_Nunzio=somma_Nunzio + i

	lunghezza_Nunzio=len(voti_Nunzio)

	media_Nunzio= somma_Nunzio/lunghezza_Nunzio

print('')

if nome=="Enzo":

	print('')
	print('I voti di Enzo sono:')

	for i in voti_Enzo:

		print(i)

	print('')

	print('I voti insufficienti di Enzo sono:')

	for i in voti_insuf_Enzo:

		print(i)
	
	print('la media di Enzo è ' , media_Enzo)

	if media_Enzo<6:

		print('La media di Enzo è insufficiente')

if nome=="Nunzio":

	print('')
	print('I voti di Nunzio sono:')

	for i in voti_Nunzio:

		print(i)

	print('')

	print('I voti insufficienti di Nunzio sono:')

	for i in voti_insuf_Nunzio:

		print(i)
	
	print('la media di Nunzio è ' , media_Nunzio)

	if media_Nunzio<6:

		print('La media di Nunzio è insufficiente')

if media_Enzo<media_Nunzio:

	print('Nunzio ha una media superiore a Enzo')

else:
	print('Enzio ha una media superiore a Nunzio')

data= randint(22,30)

print('I due studenti vanno interrogati il ' , data , ' maggio')