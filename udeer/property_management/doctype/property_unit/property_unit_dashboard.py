from frappe import _


def get_data():
    return {
        'fieldname':
        'property_unit',
        'transactions': [{
            'label': _('Leases'),
            'items': ['Lease']
        }, {
            'label': _('Payment'),
            'items': ['Unit Expense']
        }]
    }
