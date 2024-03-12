# Crear un ambiente python

Para crear un ambiente python se debe instalar la librería venv. Una vez instalada, se procede en consola con lo siguiente:

Vaya hasta la carpeta donde quiere crear el entorno

```bash
python -m venv nombre_del_entorno
```

En mi caso, el comando es:

```bash
python -m venv venv
```

Para activarlo, usamos el siguiente comando:

```bash
source venv/bin/activate
```
 Y para desactivarlo:
 
```bash
source venv/bin/deactivate
```

Nota: Dentro de pycharm debe ir a la parte inferior dera (interpreter settings) y configurar el ambiente creado. Luego puede ir a la parte superior (edit configurations) y asignar el ambiente ya creado.