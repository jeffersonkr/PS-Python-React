# Game ecommerce API:
Ecommerce api for games

-----------------------------------------------------------------
## HOW TO START:

1. Clone this repository.
    - `git clone git@github.com:jeffersonkr/PS-Python-React.git`

2. In the terminal go to the directory of repository.
3. Run docker composer (Docker Compose version v2.16.0)
    - `docker-compose up --build`

-----------------------------------------------------------------
## HOW TO TEST:

1. with project running, get into backend container.
2. Run pytest
    - `pytest`

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
Route to change password.

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
Route to register an customer.

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
Route to all update data of an user.

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
Route to update specific data of an user.

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
Route to login an get token.

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
Route do logout.

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
Route to logout from all devices.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

### /market/cart/

#### POST
##### Description
Route to add a cart.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| data | body |  | Yes | [Cart](#cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Cart](#cart) |

### /market/cart/{id}

#### GET
##### Description
Route to get a cart

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A unique integer value identifying this cart. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#cart) |

#### PUT
##### Description
route to update all data of a cart.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A unique integer value identifying this cart. | Yes | integer |
| data | body |  | Yes | [Cart](#cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#cart) |

#### PATCH
##### Description
Route to update a cart.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A unique integer value identifying this cart. | Yes | integer |
| data | body |  | Yes | [Cart](#cart) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Cart](#cart) |

### /market/product/

#### GET
##### Description
Route to get all products.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Product](#product) ] |

### /market/purchase/

#### POST
##### Description
Route to create a order.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| data | body |  | Yes | [Purchase](#purchase) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Purchase](#purchase) |

### /market/purchase/{id}

#### GET
##### Description
Route to get specific order

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| id | path | A unique integer value identifying this purchase. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Purchase](#purchase) |

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

#### Cart

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| purchase | integer |  | Yes |
| product | integer |  | Yes |
| quantity | integer |  | Yes |
| price | string (decimal) |  | Yes |

#### Product

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| price | string (decimal) |  | Yes |
| score | integer |  | Yes |
| image | string |  | No |

#### Purchase

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| customer | string (uuid) |  | Yes |
| created | dateTime |  | Yes |
