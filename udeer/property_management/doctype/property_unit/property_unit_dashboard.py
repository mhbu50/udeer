from frappe import _


def get_data():
    return {
        'fieldname':
        'property_unit',
        'transactions': [{
            'label': _('Leases'),
            'items': ['Lease']
        }, {
            'label': _('Expenses'),
            'items': ["Property Expense"]
        },{
            'label': _('Maintenance'),
            'items': ["Maintenance Schedule","Maintenance Visit"]
        }]
    }
