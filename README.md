# Django example project for using django-cognito-lowlevel

This is an example code for using the [django-cognito-lowlevel](https://github.com/pulsely/django-cognito-lowlevel), which is a Django package for handling authentication with AWS Cognito in a lower level way.

---

## Quick Start

Here is how to run this test project with Python version 3.9+.  
(Your Python 3 runtime could be named differently, such as 'python3', so change to ``python3 -m venv venv`` if this is the case.)


```sh
git clone https://github.com/pulsely/django-cognito-lowlevel
cd django-cognito-lowlevel
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt 
python manage.py runserver
```

The Django project will exit immediately if you did not setup the COGNITO configurations. A sample settings will be printed on console for you.

Now, modify the settings at ``cognitolowlevelexample/settings.py`` and you will be good to go.

---

### Django settings that should and can be configured

The following variables are needed at the **settings.py** of your project.

| **Varaiable**                       | **Description & example**                                                                                                                            |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `COGNITO_USER_POOL_ID`              | User pool ID of your AWS Cognito setup. <br />e.g. `"eu-west-XXXXXXXX"`                                                                              |
| `COGNITO_CLIENT_ID`                 | Client ID of your AWS Cognito setup. <br />e.g. `"2vvdsdfr243rwefswe445rte5edr"`                                                                     |
| `COGNITO_APP_CLIENT_SECRET`         | Client Secret of AWS Cognito setup. <br />e.g. `1urj4uktvlmb0pps234234d6io8tipmrlu3se13fdssdf`                                                       |
| `COGNITO_TOKEN_URL`                 | The Token URL of your AWS Cognito setup. <br />e.g. `"https://<xxxxxxxxxx>.auth.<eu-west-2>.amazoncognito.com/oauth2/token"`                         |
| `COGNIT_CALLBACK_URL_PATH`          | Call back path redirected from AWS Cognito. <br />e.g. `"some-folder-of-your-choice/api/cognito/userpool/callback/"`                                 |
| `COGNITO_REDIRECT_URL`              | Add some random delay of 1 to 30 seconds for each HTTP requests. Disable by default. <br />e.g.`f"http://localhost:8000/{COGNIT_CALLBACK_URL_PATH}"` |
| `COGNITO_HOST`                      | The host of your AWS Cognito setup. <br />e.g. `"<xxxxxxxxxx>.auth.<eu-west-2>.amazoncognito.com"`                                                   |
| `COGNITO_USERPOOL_REGION`           | Default AWS Cognito region Name. <br />e.g.`"us-west-2"`                                                                                             |
| `COGNITO_AUTH_SUCCESS_REDIRECT_URL` | URL or Django URL route name of redirection upon success, after obtaining the `access_token` and `id_token`. <br />e.g. `"landing:index"`            |
| `COGNITO_AUTH_ERROR_REDIRECT_URL`   | URL or Django URL route name of redirection upon error. <br />e.g.`"landing:error"`                                                                  |
| `COGNITO_PUBLIC_KEYS_CACHE_TIMEOUT` | Cache time of the public keys of your AWS Cognito setup. <br />e.g.`300`                                                                             |

---

# Credits & Acknowledgements

### Python packages dependencies

- **awslabs/aws-support-tools**  
  Decode and verify Amazon Cognito JWT tokens  
  Copyright (c) Amazon Web Services - Labs
  Apache-2.0 license
  https://github.com/awslabs/aws-support-tools/tree/master/Cognito/decode-verify-jwt

- **Django**  
  Copyright (c) Django Software Foundation and individual contributors.  
  All rights reserved.  
  https://www.djangoproject.com/

- **Requests**  
  Copyright (c) Kenneth Reitz & Python Software Foundation
  Apache-2.0 license
  https://github.com/psf/requests

- **colorama**  
  Copyright Jonathan Hartley & Arnon Yaari, 2013-2020.
  BSD-3-Clause license
  https://github.com/tartley/colorama

- **python-jose**  
  Copyright (c) Michael Davis
  MIT license
  https://github.com/mpdavis/python-jose

---

## License

Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
