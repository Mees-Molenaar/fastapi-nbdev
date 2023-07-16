# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

Enjoy!

##

Dev Huddle (02FEB23)

nbdev repository aanmaken:
Op Github een repository maken (als je Github pages wilt dan een publieke repo)
Ook belangrijk is dat de naam niet met underscores is maar met hyphens, met je package name worden de hyphens dan verandert naar underscores
Maak een venv aan in je project folder
installeer nbdev
vervolgens installeer je quarto met een nbdev commando: nbdev_install_quarto
Nu clone je je git repo
Dan run je nbdev_new om je repository op te zetten en dat commit je
Als je Github pages voor je documentatie wilt gebruiken, dan kan je dat nu doen.
Dan kunnen we via Github pages de docs bekijken
Je kunt je docs ook lokaal previewen met nbdev_preview

Om makkelijker te developen wil je ook je package installeren in je venv:
Eerst modules creeeren van je notebooks nbdev_export
Dan deze pip command:
Pip install -e ‘.[dev]’
-e staat voor editable waardoor wijzigingen in je package meteen opgepakt worden door pip
en met [dev] installeer je ook dev dependencies

FASTAPI opzetten in nbdev:
fastapi[all] toevoegen als dependencies in settings.ini (ik weet niet meer 100% zeker of die dan ook mee gaat door die pip install -e, anders ook pip install fastapi[all]
Dan gaan we een hele simpele Fastapi maken met een route naar ‘/‘
nbdev_prepare uitvoeren:
export notebooks naar modules
cleans notebooks (nodig voor github)
runs tests (als je ze heb)
En rendert index.ipynb naar je README (handig als je die geupdate hebt)
En dan laten zien hoe docs eruitziet en laten zien dat het werkt
API runnen met uvicorn command:
uvicorn fastapi_nbdev.main:app --reload

Nu een test toe voegen
request library aan dependcies toevoegen (en misschien weer pip install requests)
En dan de test schrijven door:
fastcore_test the importeren from fastcore_test import \*
En dan test_eq() functie te gebruiken, want die laat ook diffs zien
Dan nbdev_prepare
Dan zie je nu dat de test het haalt

Dan een extra route toevoegen als voorbeeld

Nu gaan we dit deployen naar AWS
Ik wil dat doen met API Gateway en Lambdas, want je hebt voor
API Gateway: 1 miioen requests gratis
Lambda: Ook 1 milioen requests free tier
En dan is het serverless (dus zeer weinig configuraties)
Rest is betalen voor wat je gebruik, ook chill geen extra kosten

Lambda functie
De lambda functie wordt eigenlijk een hele kleine Fastapi app met de gemaakte route
En we gebruiken een package: Mangum
Deze package doet het volgende:
Zet een request (bijvoorbeeld API GATEWAY) om naar een ASGI request

Bovenstaande app bundelen naar een .zip
Hier heb ik een bash script voor (deze even doornemen)

Dan pak ik de infra code dat ik al geschreven heb
En dat dan samen doornemen

Als het goed is kan ik dat dan deployen met de volgende command:
cdk synth -> maakt Cloudformation templates van je app
cdk deploy -> Deployd (duh)
