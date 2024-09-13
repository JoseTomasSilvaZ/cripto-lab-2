## Laboratorio 2 - Criptografía 🐍🦈

Este repositorio contiene los scripts de Python y Shell utilizados para la realización del laboratorio 2 del ramo Criptografía y Seguridad en Redes de la Universidad Diego Portales.
Este laboratorio se enfoca en métodos de ataques de fuerza bruta utilizando distintas herramientas para el análisis y ejecución del ataque.
Se hace uso de [Wireshark](https://www.wireshark.org/download.html) para sniffing de la red, [BurpSuite](https://portswigger.net/burp) como proxy y como una de las herramientas de ejecución del ataque, como también [THC - Hydra](https://github.com/vanhauser-thc/thc-hydra) y cURL para este último motivo. 

Para obtener un entorno ético y seguro para realizar pruebas, se utiliza [DVWA](https://github.com/digininja/DVWA).

### Setup

Clona el repositorio

```bash
git clone https://github.com/JoseTomasSilvaZ/cripto-lab-2
cd cripto-lab-2
```
#### Shell scripts

Agrega los permisos necesarios a los shell scripts

```bash
chmod +x curl.sh
chmod +x hydra.sh
```

Ejecuta el script que necesites

```bash
./curl.sh
./hydra.sh
```

#### Python

Crea e ingresa a tu entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

Instala las dependencias 

```bash
pip install -r requirements.txt
```

Ejecuta el script

```bash
python brute_force.py
```