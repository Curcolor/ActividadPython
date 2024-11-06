# Talento tech Caribe
## Identificadores de extensiones de que me gustaron que están en el computador de la sala 6
________________________________________________________________

blackboxapp.blackbox
enkia.tokyo-night
esbenp.prettier-vscode
ms-ceintl.vscode-language-pack-es
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
redhat.java
ritwickdey.liveserver
sdras.night-owl
tabnine.tabnine-vscode
usernamehw.errorlens
vaporizer.vaporizer-dark
visualstudioexptteam.intellicode-api-usage-examples
visualstudioexptteam.vscodeintellicode
vscjava.vscode-gradle
vscjava.vscode-java-debug
vscjava.vscode-java-dependency
vscjava.vscode-java-pack
vscjava.vscode-java-test
vscjava.vscode-maven
________________________________________________________________

## Pasos para instalarlos de forma automatica: 
Lo primero es copiar todos esos identificadores de extensión, y luego introducir el siguiente **script** de _bash_.
```bash
# Ver mis propias extensiones para comparar:
code --list-extensions > extensions.txt
# Instalación:
cat extensions.txt | xargs -n 1 code --install-extension
```
al copiar todos los identificadores de extensión se deben introducir en un archivo _.txt_ en el script solo reconocerá el nombre _"extensions"_, se puede cambair si se modifica el script.
