Para crear el entorno virtual: 
- virtualenv -p python3 env

Para activar el entorno virtual: 
./env/Scripts/activate

Si no funciona:
Habilitar la ejecución de scripts:
Abre PowerShell como administrador y ejecuta el siguiente comando para habilitar la ejecución de scripts:
Set-ExecutionPolicy RemoteSigned
Esto permitirá la ejecución de scripts locales firmados, mientras que los scripts descargados desde Internet deben tener una firma digital válida.

Vuelve a intentar ejecutar el script:
Después de cambiar la política de ejecución, intenta nuevamente ejecutar el script con el comando:
.\activate

tiene que aparecer (env) PS C:/etc, etc

Desactivar el entorno virual:
desactivate