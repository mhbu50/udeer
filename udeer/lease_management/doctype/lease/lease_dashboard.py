from frappe import _


def get_data():
    return {
        'fieldname':
        'lease',
        'transactions': [{
            'label': _('Property & Unit'),
            'items': ['Lease Rent Payment', "Lease Installment"]
        }]
    }
