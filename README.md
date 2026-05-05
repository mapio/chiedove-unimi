Chi e dove @ UniMI
==================

Strumento da riga di comando per interrogare la rubrica
[Chi e dove](https://www.unimi.it/it/chi-e-dove) dell'Università degli Studi di Milano.

Dato un cognome, recupera per ogni persona trovata: nome, sede di lavoro,
numeri di telefono e indirizzi email.

## Utilizzo

```
chiedove_unimi <cognome>
```

### Esempio

```
$ chiedove_unimi santini
Santini Benedetta
	Phone(s): 0250314073
	Email(s): benedetta.santini@unimi.it
Santini Emiliano
	Phone(s): 0250312115
	Email(s): emiliano.santini@unimi.it
Santini Massimo
	Sede: Via Celoria, 18
	Phone(s): 0250316259
	Email(s): massimo.santini@unimi.it, santini@di.unimi.it
```

## Installazione

Scaricare il file `chiedove_unimi` dall'ultima release disponibile nella pagina
[Releases](https://github.com/mapio/chiedove-unimi/releases/latest), renderlo
eseguibile e copiarlo in una directory nel `PATH`:

```
chmod +x chiedove_unimi
mv chiedove_unimi ~/.local/bin/
```

È richiesto Python 3.
