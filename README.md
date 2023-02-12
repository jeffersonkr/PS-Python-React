# Game ecommerce API:
Ecommerce api for games

-----------------------------------------------------------------
## HOW TO START:

1. Clone this repository.
    - `git clone git@github.com:jeffersonkr/PS-Python-React.git`

2. In the terminal go to the directory of repository.
3. Run docker composer
    - `docker-compose up --build`
    
-----------------------------------------------------------------
## API Routes:

### Security
**Bearer**  

| apiKey | *API Key* |
| ------ | --------- |
| In | header |
| Name | Authorization |

### /accounts/change_password/{id}/

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A UUID string identifying this user. | Yes | string (uuid) |
| data | body |  | Yes | [ChangePassword](#changepassword) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ChangePassword](#changepassword) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A UUID string identifying this user. | Yes | string (uuid) |
| data | body |  | Yes | [ChangePassword](#changepassword) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ChangePassword](#changepassword) |

### /accounts/register/

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| data | body |  | Yes | [Register](#register) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Register](#register) |

### /accounts/update_profile/{id}/

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A UUID string identifying this user. | Yes | string (uuid) |
| data | body |  | Yes | [UpdateUser](#updateuser) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [UpdateUser](#updateuser) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A UUID string identifying this user. | Yes | string (uuid) |
| data | body |  | Yes | [UpdateUser](#updateuser) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [UpdateUser](#updateuser) |

### /authentication/login/

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| data | body |  | Yes | [MyTokenObtainPair](#mytokenobtainpair) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [MyTokenObtainPair](#mytokenobtainpair) |

### /authentication/login/refresh/

#### POST
##### Description

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| data | body |  | Yes | [TokenRefresh](#tokenrefresh) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenRefresh](#tokenrefresh) |

### /authentication/logout/

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### /authentication/logout_all/

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### Models

#### ChangePassword

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| old_password | string |  | Yes |
| password | string |  | Yes |
| password2 | string |  | Yes |

#### Register

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| password | string |  | Yes |
| password2 | string |  | Yes |
| email | string (email) |  | Yes |
| full_name | string |  | Yes |
| bio | string |  | No |
| birth_date | date |  | No |

#### UpdateUser

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| email | string (email) |  | Yes |
| full_name | string |  | No |
| bio | string |  | No |
| birth_date | date |  | No |

#### MyTokenObtainPair

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| email | string |  | Yes |
| password | string |  | Yes |

#### TokenRefresh

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| refresh | string |  | Yes |
| access | string |  | No |
