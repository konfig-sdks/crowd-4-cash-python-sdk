<div align="center">

[![Visit Crowd4cash](./header.png)](https://crowd4cash.ch&#x2F;)

# Crowd4cash<a id="crowd4cash"></a>

Access to the Crowd4Cash Crowdlending Platform through an API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`crowd4cash.application.set_definitive_handover_date`](#crowd4cashapplicationset_definitive_handover_date)
  * [`crowd4cash.application.submit_loan_application`](#crowd4cashapplicationsubmit_loan_application)
  * [`crowd4cash.application.submit_partner_loan_application`](#crowd4cashapplicationsubmit_partner_loan_application)
  * [`crowd4cash.application.submit_rental_loan_application`](#crowd4cashapplicationsubmit_rental_loan_application)
  * [`crowd4cash.authentication.get_token`](#crowd4cashauthenticationget_token)
  * [`crowd4cash.bidding.place_bid`](#crowd4cashbiddingplace_bid)
  * [`crowd4cash.bidding.submit_bids`](#crowd4cashbiddingsubmit_bids)
  * [`crowd4cash.contracts.get_all`](#crowd4cashcontractsget_all)
  * [`crowd4cash.contracts.get_loan_contract`](#crowd4cashcontractsget_loan_contract)
  * [`crowd4cash.contracts.get_specific`](#crowd4cashcontractsget_specific)
  * [`crowd4cash.contracts.get_specific_intermediary_loan_contract`](#crowd4cashcontractsget_specific_intermediary_loan_contract)
  * [`crowd4cash.loans.get_loan_data`](#crowd4cashloansget_loan_data)
  * [`crowd4cash.opportunities.get_available_investments`](#crowd4cashopportunitiesget_available_investments)
  * [`crowd4cash.portfolio.get_customized_portfolio`](#crowd4cashportfolioget_customized_portfolio)
  * [`crowd4cash.portfolio.get_investments`](#crowd4cashportfolioget_investments)
  * [`crowd4cash.reports.get_connector_investments`](#crowd4cashreportsget_connector_investments)
  * [`crowd4cash.reports.get_intermediary_data`](#crowd4cashreportsget_intermediary_data)
  * [`crowd4cash.reports.rental_account_summary`](#crowd4cashreportsrental_account_summary)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Crowd4Cash&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from crowd_4_cash_python_sdk import Crowd4Cash, ApiException

crowd4cash = Crowd4Cash(
    bearer="YOUR_API_KEY",
)

try:
    # Set the definitive Handover Date (a date when the item is handed over to the customer)
    set_definitive_handover_date_response = (
        crowd4cash.application.set_definitive_handover_date(
            loan_id=4989,
            handover_date="25.01.2023",
        )
    )
    print(set_definitive_handover_date_response)
except ApiException as e:
    print(
        "Exception when calling ApplicationApi.set_definitive_handover_date: %s\n" % e
    )
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["type"])
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["type"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from crowd_4_cash_python_sdk import Crowd4Cash, ApiException

crowd4cash = Crowd4Cash(
    bearer="YOUR_API_KEY",
)


async def main():
    try:
        # Set the definitive Handover Date (a date when the item is handed over to the customer)
        set_definitive_handover_date_response = (
            await crowd4cash.application.aset_definitive_handover_date(
                loan_id=4989,
                handover_date="25.01.2023",
            )
        )
        print(set_definitive_handover_date_response)
    except ApiException as e:
        print(
            "Exception when calling ApplicationApi.set_definitive_handover_date: %s\n"
            % e
        )
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["type"])
            pprint(e.body["message"])
        if e.status == 401:
            pprint(e.body["type"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from crowd_4_cash_python_sdk import Crowd4Cash, ApiException

crowd4cash = Crowd4Cash(
    bearer="YOUR_API_KEY",
)

try:
    # Set the definitive Handover Date (a date when the item is handed over to the customer)
    set_definitive_handover_date_response = (
        crowd4cash.application.raw.set_definitive_handover_date(
            loan_id=4989,
            handover_date="25.01.2023",
        )
    )
    pprint(set_definitive_handover_date_response.body)
    pprint(set_definitive_handover_date_response.body["result"])
    pprint(set_definitive_handover_date_response.body["message"])
    pprint(set_definitive_handover_date_response.body["loan_id"])
    pprint(set_definitive_handover_date_response.body["esr"])
    pprint(set_definitive_handover_date_response.body["error"])
    pprint(set_definitive_handover_date_response.headers)
    pprint(set_definitive_handover_date_response.status)
    pprint(set_definitive_handover_date_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling ApplicationApi.set_definitive_handover_date: %s\n" % e
    )
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["type"])
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["type"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `crowd4cash.application.set_definitive_handover_date`<a id="crowd4cashapplicationset_definitive_handover_date"></a>

**Note**: It's valid only for loans made indirectly through the intermediary.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_definitive_handover_date_response = (
    crowd4cash.application.set_definitive_handover_date(
        loan_id=4989,
        handover_date="25.01.2023",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### loan_id: `int`<a id="loan_id-int"></a>

Loan ID

##### handover_date: `Optional[str]`<a id="handover_date-optionalstr"></a>

The date when the car is handed over to the subscriber

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntermediaryLoanHandoverDate`](./crowd_4_cash_python_sdk/type/intermediary_loan_handover_date.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationResult`](./crowd_4_cash_python_sdk/pydantic/application_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/IntermediaryLoan` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.application.submit_loan_application`<a id="crowd4cashapplicationsubmit_loan_application"></a>

**Note**: Approval and funding times vary, but typically it takes only 24 hours.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_loan_application_response = crowd4cash.application.submit_loan_application()
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationResult`](./crowd_4_cash_python_sdk/pydantic/application_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Loan` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.application.submit_partner_loan_application`<a id="crowd4cashapplicationsubmit_partner_loan_application"></a>

**Note**: Each successful application creates a binding obligation on you. Once you apply you may not retract the application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_partner_loan_application_response = (
    crowd4cash.application.submit_partner_loan_application(
        serial_number="WBAVB12345KS12345",
        identification_number="630.830.709",
        partner_id=12225,
        purchase_item="Car",
        item_status="Rented",
        item_name="BMW 318D e90",
        item_type="Saloon",
        item_brand="BMW",
        item_model="318D",
        item_color="Black",
        item_market_value=10000,
        manufacture_date="13.05.2020",
        first_registration="15.01.2021",
        mileage="24000 km",
        item_certificate="1AA123",
        rental_amount=420,
        handover_date="23.01.2023",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### serial_number: `str`<a id="serial_number-str"></a>

Serial number (aka VIN or Chassis No.)

##### identification_number: `str`<a id="identification_number-str"></a>

Identification number (aka Stammnummer)

##### partner_id: `int`<a id="partner_id-int"></a>

ID of the partner that is buying an item. This ID can be taken from the Report endpoint and Intermediary route.

##### purchase_item: `Optional[str]`<a id="purchase_item-optionalstr"></a>

Description of the item you buy e.g. Car

##### item_status: `Optional[str]`<a id="item_status-optionalstr"></a>

Status of the item

##### item_name: `Optional[str]`<a id="item_name-optionalstr"></a>

Name of the item

##### item_type: `Optional[str]`<a id="item_type-optionalstr"></a>

Type of the item e.g. SUV, Van, Saloon, Cabriolet etc.

##### item_brand: `Optional[str]`<a id="item_brand-optionalstr"></a>

Brand of the item

##### item_model: `Optional[str]`<a id="item_model-optionalstr"></a>

Model of the item

##### item_color: `Optional[str]`<a id="item_color-optionalstr"></a>

Color of the item

##### item_market_value: `Union[int, float]`<a id="item_market_value-unionint-float"></a>

Market value of the item you want to buy. Please notice that the Loan Amount will be 80% of this value.

##### manufacture_date: `Optional[str]`<a id="manufacture_date-optionalstr"></a>

Date when the car was manufactured

##### first_registration: `Optional[str]`<a id="first_registration-optionalstr"></a>

Date when the item was registered very first time

##### mileage: `Optional[str]`<a id="mileage-optionalstr"></a>

Mileage of the item

##### item_certificate: `Optional[str]`<a id="item_certificate-optionalstr"></a>

Certificate of the item

##### rental_amount: `Union[int, float]`<a id="rental_amount-unionint-float"></a>

Rental amount per month

##### handover_date: `Optional[str]`<a id="handover_date-optionalstr"></a>

The expected/approximate handover date (date when the car is expected to be handed over to the subscriber). Expected format: dd.MM.yyyy

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntermediaryLoanApplication`](./crowd_4_cash_python_sdk/type/intermediary_loan_application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationResult`](./crowd_4_cash_python_sdk/pydantic/application_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/IntermediaryLoan` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.application.submit_rental_loan_application`<a id="crowd4cashapplicationsubmit_rental_loan_application"></a>

**Note**: Each successful application creates a binding obligation on you. Once you apply you may not retract the application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_rental_loan_application_response = (
    crowd4cash.application.submit_rental_loan_application(
        rentee_gender="F",
        rentee_first_name="Emma",
        rentee_last_name="Müller",
        rentee_email="username@domainname.ch",
        rentee_mobile_phone_number="91100201",
        purchase_item="Electric Scooter",
        item_name="Vespino Go, 500W",
        item_market_value=10000,
        rental_amount=500,
        id_front_photo="/9j/4AAQSkZJRgABAQEASABIAAD/...",
        id_front_extension="jpg",
        id_back_photo="/9j/4AAQSkZJRgABAQEASABIAAD/...",
        id_back_extension="jpg",
        selfie_photo="/9j/4AAQSkZJRgABAQEASABIAAD/...",
        selfie_extension="jpg",
        contract_file="JVBERi0xLjUKJeLjz9MKMyAwIG9...",
        contract_file_extension="pdf",
        api_requester="Otto Schneider",
        rentee_birthdate="23.09.1972",
        rentee_street_address="Täfernstrasse",
        rentee_house_number="4",
        rentee_zip_code="5405",
        rentee_city="Dättwil",
        item_status="Rented",
        item_type="Electric Scooter",
        item_brand="Piaggio",
        item_model="Vespino Go",
        item_color="Green",
        serial_number="WBAVB12345KS12345",
        identification_number="630.830.709",
        rent_date="23.01.2023",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rentee_gender: `str`<a id="rentee_gender-str"></a>

Rentee gender acronym. M stands for male and F for female.

##### rentee_first_name: `str`<a id="rentee_first_name-str"></a>

First name of the rentee

##### rentee_last_name: `str`<a id="rentee_last_name-str"></a>

Last name of the rentee

##### rentee_email: `str`<a id="rentee_email-str"></a>

E-mail address of the rentee

##### rentee_mobile_phone_number: `str`<a id="rentee_mobile_phone_number-str"></a>

Rentee mobile phone number - the last 8 digits only

##### purchase_item: `str`<a id="purchase_item-str"></a>

Description of the item you buy

##### item_name: `str`<a id="item_name-str"></a>

Name of the item

##### item_market_value: `Union[int, float]`<a id="item_market_value-unionint-float"></a>

Market value of the item that is rented.

##### rental_amount: `Union[int, float]`<a id="rental_amount-unionint-float"></a>

Rental amount per month

##### id_front_photo: `str`<a id="id_front_photo-str"></a>

Front Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.

##### id_front_extension: `str`<a id="id_front_extension-str"></a>

Front Side file extension.

##### id_back_photo: `str`<a id="id_back_photo-str"></a>

Back Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.

##### id_back_extension: `str`<a id="id_back_extension-str"></a>

Back Side file extension.

##### selfie_photo: `str`<a id="selfie_photo-str"></a>

Selfie of the Rentee. Please notice that you must first convert it to Base64 and then send to our API.

##### selfie_extension: `str`<a id="selfie_extension-str"></a>

Selfie file extension.

##### contract_file: `str`<a id="contract_file-str"></a>

Copy of the Contract. Please notice that you must first convert it to Base64 and then send to our API.

##### contract_file_extension: `str`<a id="contract_file_extension-str"></a>

Contract file extension.

##### api_requester: `Optional[str]`<a id="api_requester-optionalstr"></a>

Name or E-mail of the user who makes the API call

##### rentee_birthdate: `Optional[str]`<a id="rentee_birthdate-optionalstr"></a>

Birthdate of the rentee. Expected format: dd.MM.yyyy

##### rentee_street_address: `Optional[str]`<a id="rentee_street_address-optionalstr"></a>

Street address of the rentee

##### rentee_house_number: `Optional[str]`<a id="rentee_house_number-optionalstr"></a>

House number of the rentee

##### rentee_zip_code: `Optional[str]`<a id="rentee_zip_code-optionalstr"></a>

Zip code of the rentee

##### rentee_city: `Optional[str]`<a id="rentee_city-optionalstr"></a>

City of the rentee

##### item_status: `Optional[str]`<a id="item_status-optionalstr"></a>

Status of the item

##### item_type: `Optional[str]`<a id="item_type-optionalstr"></a>

Type of the item e.g. Electric Scooter, E-Motorcycle etc.

##### item_brand: `Optional[str]`<a id="item_brand-optionalstr"></a>

Brand of the item

##### item_model: `Optional[str]`<a id="item_model-optionalstr"></a>

Model of the item

##### item_color: `Optional[str]`<a id="item_color-optionalstr"></a>

Color of the item

##### serial_number: `Optional[str]`<a id="serial_number-optionalstr"></a>

Serial number (aka VIN or Chassis No.)

##### identification_number: `Optional[str]`<a id="identification_number-optionalstr"></a>

Identification number (aka Stammnummer)

##### rent_date: `Optional[str]`<a id="rent_date-optionalstr"></a>

The first date of the rental period. Expected format: dd.MM.yyyy

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RentalLoanApplication`](./crowd_4_cash_python_sdk/type/rental_loan_application.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RentalApplicationResult`](./crowd_4_cash_python_sdk/pydantic/rental_application_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/RentalLoan` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.authentication.get_token`<a id="crowd4cashauthenticationget_token"></a>

Authenticate yourself and get an access token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_response = crowd4cash.authentication.get_token(
    username="a",
    password="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

Your C4C username

##### password: `str`<a id="password-str"></a>

Your C4C password

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Login`](./crowd_4_cash_python_sdk/type/login.py)
Your username and password

#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./crowd_4_cash_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Authenticate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.bidding.place_bid`<a id="crowd4cashbiddingplace_bid"></a>

**Note**: Each successful bid creates a binding obligation on you. Once you place you may not retract your bid.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
place_bid_response = crowd4cash.bidding.place_bid(
    loan_id=1,
    amount=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### loan_id: `int`<a id="loan_id-int"></a>

Loan ID which you want to invest in

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount of the bid

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Bid`](./crowd_4_cash_python_sdk/type/bid.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BiddingResult`](./crowd_4_cash_python_sdk/pydantic/bidding_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Bid` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.bidding.submit_bids`<a id="crowd4cashbiddingsubmit_bids"></a>

**Note**: Crowd4Cash allows you to invest as agent on behalf of other investors. You can submit multiple bids on the same request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_bids_response = crowd4cash.bidding.submit_bids(
    body=[
        {
            "investor_id": 570,
            "loan_id": 3201,
            "amount": 12000,
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BiddingSubmitBidsRequest`](./crowd_4_cash_python_sdk/type/bidding_submit_bids_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MultipleBiddingResult`](./crowd_4_cash_python_sdk/pydantic/multiple_bidding_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Bids` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.contracts.get_all`<a id="crowd4cashcontractsget_all"></a>

Get all your contracts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = crowd4cash.contracts.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Contract`](./crowd_4_cash_python_sdk/pydantic/contract.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Contracts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.contracts.get_loan_contract`<a id="crowd4cashcontractsget_loan_contract"></a>

Get specific rental loan contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_loan_contract_response = crowd4cash.contracts.get_loan_contract(
    loan_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### loan_id: `int`<a id="loan_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Contract`](./crowd_4_cash_python_sdk/pydantic/contract.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Contracts/RentalLoan/{loanId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.contracts.get_specific`<a id="crowd4cashcontractsget_specific"></a>

Get specific contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_response = crowd4cash.contracts.get_specific(
    loan_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### loan_id: `int`<a id="loan_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Contract`](./crowd_4_cash_python_sdk/pydantic/contract.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Contracts/{loanId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.contracts.get_specific_intermediary_loan_contract`<a id="crowd4cashcontractsget_specific_intermediary_loan_contract"></a>

Get specific intermediary loan contract

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_intermediary_loan_contract_response = (
    crowd4cash.contracts.get_specific_intermediary_loan_contract(
        partner_id=1,
        loan_id=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partner_id: `int`<a id="partner_id-int"></a>

##### loan_id: `int`<a id="loan_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Contract`](./crowd_4_cash_python_sdk/pydantic/contract.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Contracts/{partnerId}/{loanId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.loans.get_loan_data`<a id="crowd4cashloansget_loan_data"></a>

**Note**: In order to consume this endpoint we need to grant a special access to your account. Please [contact us](https://crowd4cash.ch/contact) for further information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_loan_data_response = crowd4cash.loans.get_loan_data(
    page_number=1,
    page_size=1,
    loanstatus="All",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number you want to access

##### page_size: `int`<a id="page_size-int"></a>

Number of items per page. Max is 20

##### loanstatus: [`Status`](./crowd_4_cash_python_sdk/type/.py)<a id="loanstatus-statuscrowd_4_cash_python_sdktypepy"></a>

Status values that need to be considered for filter

#### 🔄 Return<a id="🔄-return"></a>

[`PagedList`](./crowd_4_cash_python_sdk/pydantic/paged_list.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Loans` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.opportunities.get_available_investments`<a id="crowd4cashopportunitiesget_available_investments"></a>

__Note__: C4C offers a private, secure and uncomplicated way for the investors to discover, analyze, review and invest.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_investments_response = crowd4cash.opportunities.get_available_investments(
    rating="AA",
    loan_amount=3.14,
    loan_type="string_example",
    available_amount=3.14,
    interest_rate=3.14,
    duration=1,
    insurance="false",
    collateral="false",
    borrower_age=1,
    borrower_nationality="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### rating: [`LoanRating`](./crowd_4_cash_python_sdk/type/.py)<a id="rating-loanratingcrowd_4_cash_python_sdktypepy"></a>

Evaluation of the credit risk based on a borrower's credit history, quality of the collateral, and the likelihood of repayment e.g. AA

##### loan_amount: `Union[int, float]`<a id="loan_amount-unionint-float"></a>

Loan amount e.g. 25000

##### loan_type: `str`<a id="loan_type-str"></a>

Type of the loan e.g. Private, SME

##### available_amount: `Union[int, float]`<a id="available_amount-unionint-float"></a>

Available amount to be invested at the moment of our API consuming e.g. 2000

##### interest_rate: `Union[int, float]`<a id="interest_rate-unionint-float"></a>

Interest rate of the loan in % e.g. 5.6

##### duration: `int`<a id="duration-int"></a>

Duration in months e.g. 24

##### insurance: [`YN`](./crowd_4_cash_python_sdk/type/.py)<a id="insurance-yncrowd_4_cash_python_sdktypepy"></a>

Is loan issured? - Yes, No

##### collateral: [`YN`](./crowd_4_cash_python_sdk/type/.py)<a id="collateral-yncrowd_4_cash_python_sdktypepy"></a>

Is loan collaterialized? - Yes, No

##### borrower_age: `int`<a id="borrower_age-int"></a>

Age of the borrower e.g. 42

##### borrower_nationality: `str`<a id="borrower_nationality-str"></a>

Nationality of the borrower, e.g Switzerland, Liechtenstein ...

#### 🔄 Return<a id="🔄-return"></a>

[`Opportunity`](./crowd_4_cash_python_sdk/pydantic/opportunity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Opportunities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.portfolio.get_customized_portfolio`<a id="crowd4cashportfolioget_customized_portfolio"></a>

__Note__: If the standard portfolio doesn't suit your needs, please [contact C4C](https://crowd4cash.ch/contact) to request customization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customized_portfolio_response = crowd4cash.portfolio.get_customized_portfolio(
    _from="string_example",
    to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

##### to: `str`<a id="to-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Portfolio`](./crowd_4_cash_python_sdk/pydantic/portfolio.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CustomPortfolio` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.portfolio.get_investments`<a id="crowd4cashportfolioget_investments"></a>

Get your investment portfolio

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_investments_response = crowd4cash.portfolio.get_investments(
    _from="string_example",
    to="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `str`<a id="_from-str"></a>

##### to: `str`<a id="to-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Portfolio`](./crowd_4_cash_python_sdk/pydantic/portfolio.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Portfolio` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.reports.get_connector_investments`<a id="crowd4cashreportsget_connector_investments"></a>

__Note__: It's valid only for investments made indirectly through connector

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_connector_investments_response = crowd4cash.reports.get_connector_investments()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorReport`](./crowd_4_cash_python_sdk/pydantic/connector_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Connector` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.reports.get_intermediary_data`<a id="crowd4cashreportsget_intermediary_data"></a>

__Note__: It's valid only for loans made indirectly through the intermediary

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_intermediary_data_response = crowd4cash.reports.get_intermediary_data()
```

#### 🔄 Return<a id="🔄-return"></a>

[`IntermediaryReport`](./crowd_4_cash_python_sdk/pydantic/intermediary_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Intermediary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `crowd4cash.reports.rental_account_summary`<a id="crowd4cashreportsrental_account_summary"></a>

__Note__: It's valid only for loans made through this API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rental_account_summary_response = crowd4cash.reports.rental_account_summary()
```

#### 🔄 Return<a id="🔄-return"></a>

[`RentalReport`](./crowd_4_cash_python_sdk/pydantic/rental_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Rental` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
