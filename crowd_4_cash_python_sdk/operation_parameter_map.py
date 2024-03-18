operation_parameter_map = {
    '/IntermediaryLoan-PUT': {
        'parameters': [
            {
                'name': 'loanId'
            },
            {
                'name': 'handoverDate'
            },
        ]
    },
    '/Loan-POST': {
        'parameters': [
        ]
    },
    '/IntermediaryLoan-POST': {
        'parameters': [
            {
                'name': 'serialNumber'
            },
            {
                'name': 'identificationNumber'
            },
            {
                'name': 'partnerId'
            },
            {
                'name': 'purchaseItem'
            },
            {
                'name': 'itemStatus'
            },
            {
                'name': 'itemName'
            },
            {
                'name': 'itemType'
            },
            {
                'name': 'itemBrand'
            },
            {
                'name': 'itemModel'
            },
            {
                'name': 'itemColor'
            },
            {
                'name': 'itemMarketValue'
            },
            {
                'name': 'manufactureDate'
            },
            {
                'name': 'firstRegistration'
            },
            {
                'name': 'mileage'
            },
            {
                'name': 'itemCertificate'
            },
            {
                'name': 'rentalAmount'
            },
            {
                'name': 'handoverDate'
            },
        ]
    },
    '/RentalLoan-POST': {
        'parameters': [
            {
                'name': 'renteeGender'
            },
            {
                'name': 'renteeFirstName'
            },
            {
                'name': 'renteeLastName'
            },
            {
                'name': 'renteeEmail'
            },
            {
                'name': 'renteeMobilePhoneNumber'
            },
            {
                'name': 'purchaseItem'
            },
            {
                'name': 'itemName'
            },
            {
                'name': 'itemMarketValue'
            },
            {
                'name': 'rentalAmount'
            },
            {
                'name': 'idFrontPhoto'
            },
            {
                'name': 'idFrontExtension'
            },
            {
                'name': 'idBackPhoto'
            },
            {
                'name': 'idBackExtension'
            },
            {
                'name': 'selfiePhoto'
            },
            {
                'name': 'selfieExtension'
            },
            {
                'name': 'contractFile'
            },
            {
                'name': 'contractFileExtension'
            },
            {
                'name': 'apiRequester'
            },
            {
                'name': 'renteeBirthdate'
            },
            {
                'name': 'renteeStreetAddress'
            },
            {
                'name': 'renteeHouseNumber'
            },
            {
                'name': 'renteeZipCode'
            },
            {
                'name': 'renteeCity'
            },
            {
                'name': 'itemStatus'
            },
            {
                'name': 'itemType'
            },
            {
                'name': 'itemBrand'
            },
            {
                'name': 'itemModel'
            },
            {
                'name': 'itemColor'
            },
            {
                'name': 'serialNumber'
            },
            {
                'name': 'identificationNumber'
            },
            {
                'name': 'rentDate'
            },
        ]
    },
    '/Authenticate-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/Bid-POST': {
        'parameters': [
            {
                'name': 'loanId'
            },
            {
                'name': 'amount'
            },
        ]
    },
    '/Bids-POST': {
        'parameters': [
        ]
    },
    '/Contracts-GET': {
        'parameters': [
        ]
    },
    '/Contracts/RentalLoan/{loanId}-GET': {
        'parameters': [
            {
                'name': 'loanId'
            },
        ]
    },
    '/Contracts/{loanId}-GET': {
        'parameters': [
            {
                'name': 'loanId'
            },
        ]
    },
    '/Contracts/{partnerId}/{loanId}-GET': {
        'parameters': [
            {
                'name': 'partnerId'
            },
            {
                'name': 'loanId'
            },
        ]
    },
    '/Loans-GET': {
        'parameters': [
            {
                'name': 'PageNumber'
            },
            {
                'name': 'PageSize'
            },
            {
                'name': 'loanstatus'
            },
        ]
    },
    '/Opportunities-GET': {
        'parameters': [
            {
                'name': 'Rating'
            },
            {
                'name': 'LoanAmount'
            },
            {
                'name': 'LoanType'
            },
            {
                'name': 'AvailableAmount'
            },
            {
                'name': 'InterestRate'
            },
            {
                'name': 'Duration'
            },
            {
                'name': 'Insurance'
            },
            {
                'name': 'Collateral'
            },
            {
                'name': 'BorrowerAge'
            },
            {
                'name': 'BorrowerNationality'
            },
        ]
    },
    '/CustomPortfolio-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/Portfolio-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/Connector-GET': {
        'parameters': [
        ]
    },
    '/Intermediary-GET': {
        'parameters': [
        ]
    },
    '/Rental-GET': {
        'parameters': [
        ]
    },
};