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

Utilizando el acript de python `01-create-workspace.py` se creo el siguiente ambiente:


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

### Registro del Modelo

Se registró el modelo ejecutando el script ´07-azure-model-registration.py´:

![ModelReg](https://user-images.githubusercontent.com/78625501/141685994-8c2d9241-dcf7-4648-8194-dda3a735f1c3.JPG)

![ModelReg2](https://user-images.githubusercontent.com/78625501/141686027-81b976ec-290c-4baa-a7cf-3eb3954d0c41.JPG)

### Despliegue del modelo

Se creo el ´score.py´, el cual sera usado por el endpoint para su predicción.
Se ejecuto el script ´09-deploy-azure-model-aci.py´ para desplegar el modelo en azure:

![EndPointAzure](https://user-images.githubusercontent.com/78625501/141686438-0c1b033c-6a1c-4bec-b82b-9862912cb29c.JPG)

Para probar el endpoint se hizo el siguiente request:

curl --location --request POST 'http://f3cffdf2-3379-4caa-b2b0-60acb3cb6773.eastus2.azurecontainer.io/score' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data":
        [
           [13.73, 1.5, 2.7, 22.5, 101.0, 3.0, 3.25, 0.29, 2.38, 5.7, 1.19, 2.71, 1285.0]
        ]
}'

![PostmanResult](https://user-images.githubusercontent.com/78625501/141686955-36c2e808-57af-4b1b-9a69-cbe1d0fbc7d2.JPG)

