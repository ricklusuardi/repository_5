
lista_libri = ['Eclisse' , 'Alba Tragica' , 'Spartacus' , '2001' , 'Promessi Sposi' , 'Moby Dick' , 'Memorie di Adriano' , 'Lolita' , 'il conte di Montecristo' , 'Il Gattopardo' , '1984' , 'Cime tempestose' , 'Il processo' , 'I fratelli Karamazov']

libri_prestati = []

for i in lista_libri:

	a=lista_libri.index(i)

	if a==13:

		print(i)
	
	else:
		print(i, end= ", ")

print('')	

lista_libri.sort()

for i in lista_libri:

	a=lista_libri.index(i)

	print(a+1, lista_libri[a])

print('')
numero_libri=int(input('Quanti libri vuoi prendere in prestito? '))

n=0

print('')

while n<numero_libri:

	print('')

	b=int(input('digita il numero del libro che vuoi prendere in prestito '))

	while b<1 or b>14:
		
		if b<1:
			b=int(input('il numero è troppo piccolo, riprovare '))

		else:
			b=int(input('il numero è troppo grande, riprovare '))
		

	c=b-1
	
	libro_prestato=lista_libri[c]

	libri_prestati.append(libro_prestato)

	lista_libri.pop(c)

	print('')
	print('il libro è stato aggiunto alla lista dei libri prestati')

	n_disponibili=len(lista_libri)

	n_prestati=len(libri_prestati)

	print('')
	print('libri disponibili')
	for i in lista_libri:

		a=lista_libri.index(i)

		print(a+1 , i)

	print('')
	print('libri prestati')
	for i in libri_prestati:

		a=libri_prestati.index(i)

		print(a+1, i)

	n=n+1

