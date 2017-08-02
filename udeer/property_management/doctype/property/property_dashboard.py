from frappe import _


def get_data():
    return {
        'fieldname':
        'property',
        'transactions': [{
            'label': _('Property & Unit'),
            'items': ['Property Unit']
        }, {
            'label': _('Leases'),
            'items': ['Lease']
        }]
    }
