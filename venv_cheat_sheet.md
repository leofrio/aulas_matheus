# Guia para usar o venv
## 1 Criar o ambiente virtual 
```bash
python -m venv .venv
``` 
ou
```bash
python -m venv /path/to/new/virtual/environment
```  


## 2 Ativar o ambiente virtual 
### Linux/Mac 
```bash
source .venv/bin/activate
```  
### Windows   
```bash
.venv\Scripts\Activate.ps1 
```   
ou 
```bash
.venv\Scripts\activate.bat  
```     
ps: talvez seja necessário colocar python ou python3 antes dos comandos para os mesmos funcionarem no windows.
## 3 Instalar um pacote, depois que .venv está ativado (ex:numpy)
```bash
pip install numpy
```    
