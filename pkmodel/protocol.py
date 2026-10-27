#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=43):
        self.value = value

class IV:

    def __init__(self, dose, n_compartment=1):
        self.dose = dose  # dose function
        self.n_compartment = n_compartment  # number of compartments

    def compartment_eq(self, Qp, qc, vc, qp1, vp1):

        
