## TALLER DESPLIEGUE MODELO EN AZURE
### 1. Nombres:

- Yalila Aljure Jiménez CC 52888540
- Néstor Arbelaez CC 1128431223
- Oscar Nicolás Gómez Giraldo CC 1033337229

### Objetivos:
1. Creación Workspace en azure ml
2. Entrenamiento de un modelo utilizando la base de datos load_wine the la libreria sklearn
3. Registro del modelo 
4. Despliegue del modelo 

### Metodología:

Para e desarrollo del objetivo de este trabajo, se hará uso de la metodologia MLOPS:

![ml-lifecycle](https://user-images.githubusercontent.com/78625501/141683286-3dc5161a-d029-4d08-a74a-fb6ec1315dfb.png)


### Creacion Workspace en azure ml

Utilizando el acript de python ´01-create-workspace.py´ se creo el siguiente ambiente:


![Worksspace](https://user-images.githubusercontent.com/78625501/141684469-5f86cb10-1530-4dc3-88b9-3e204cf69ad2.JPG)

### Creacion de la maquina virtual

Utilizando el script de python ´02-create-compute.py´ se creo la siguiente maquina:

![Compute](https://user-images.githubusercontent.com/78625501/141684728-f51af5e9-8875-4afc-893b-79baf736ba16.JPG)

### Testeo del ambiente de trabajo

Utilizando el script de python ´03-test-workspace-remote.py´ se realizo la prueba del ambiente:

![PruebaWorkspace](https://user-images.githubusercontent.com/78625501/141685025-44521e6b-6472-42b2-a687-417f04970f24.JPG)

### Creación del wine model

Se creo un modelo RainForestClassifier para clasificar los diferentes tipos de vinos de la base de datos seleccionada (load_wine) utilizando el archivo de pytho ´wine-model.py´. Luego se ejecuto el script ´06-train-remote-with-remote-data.py´ y se creo el experimento en azure:

![ExperimentoWine](https://user-images.githubusercontent.com/78625501/141685793-9ffdc048-e95a-41f1-9376-cae8884d6765.JPG)




